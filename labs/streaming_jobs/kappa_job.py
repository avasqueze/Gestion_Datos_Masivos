from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
spark = (SparkSession.builder.appName('kappa-job').getOrCreate())
schema = StructType([
    StructField('event_time', StringType()),
    StructField('user_id', StringType()),
    StructField('action', StringType()),
    StructField('item_id', StringType()),
    StructField('price', DoubleType()),
    StructField('source', StringType()),
])
raw = (spark.readStream.format('kafka')
  .option('kafka.bootstrap.servers','localhost:9092')
  .option('subscribe','events')
  .option('startingOffsets','latest')
  .load())
events = (raw.selectExpr('CAST(value AS STRING) as json')
  .select(from_json(col('json'), schema).alias('e'))
  .selectExpr('e.*')
  .withColumn('event_ts', to_timestamp('event_time')))
agg = (events.withWatermark('event_ts','10 minutes')
  .groupBy(window(col('event_ts'), '1 minute'), col('action'))
  .count())
q = (agg.writeStream.format('console')
  .outputMode('update')
  .option('truncate','false')
  .start())
q.awaitTermination()
