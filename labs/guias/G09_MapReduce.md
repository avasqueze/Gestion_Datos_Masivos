# Guía — Semana 9: MapReduce con Hadoop Streaming

## WordCount
```bash
docker compose exec namenode bash -lc 'echo "hola mundo hola big data" > /tmp/wc.txt && hdfs dfs -mkdir -p /tmp/in && hdfs dfs -put -f /tmp/wc.txt /tmp/in/'
docker compose exec resourcemanager bash -lc 'yarn jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-*.jar   -D mapreduce.job.reduces=1   -input hdfs://namenode:9000/tmp/in   -output hdfs://namenode:9000/tmp/out_wc   -mapper /usr/bin/python3   -reducer /usr/bin/python3'
```
(Reemplace mapper/reducer por rutas hacia `scripts/mr_mapper.py` y `scripts/mr_reducer.py` si los copia dentro del contenedor.)

## PySpark estilo map-reduce
Use `labs/notebooks/09_mapreduce_pyspark.ipynb`.
