# Lab 1 de Big Data: Clúster con Hadoop, Hive, Spark, Zeppelin y Livy vía Docker-compose

Este lab te permitira experimentar con varias aplicaciones de big data de la forma sencilla. Idealmente, algo que pueda levantarse y desmontarse con un solo
comando.\

Iniciemos

------------------------------------------------------------------------

## Imágenes incluidas

-   Imagen base: Hadoop + Hive + Spark - [Imagen Base](https://github.com/panovvv/hadoop-hive-spark-docker)
-   Imagen Zeppelin: Interfaz de cuadernos interactivos [Imagen Zeppelin](https://github.com/panovvv/zeppelin-bigdata-docker)
-   Imagen Livy: Servidor REST para Spark - [Imagen Livy](https://github.com/panovvv/livy-docker)

------------------------------------------------------------------------

## Uso

Descargar el archivo zip desde el classroom, pasarlo a Ubuntu en WSL y descomprimirlo.

Dentro de una terminal de Ubuntu ingresar al directorio y levantar todos los servicio usando los siguiente comandos:

``` bash
cd GDM-docker-compose
docker-compose up -d
```

### Directorios importantes

* El directorio **data/** se monta en cada contenedor. Puedes usarlo como almacenamiento tanto para los archivos que quieras procesar con Hive/Spark/u otras herramientas, como para los resultados de esos cálculos.

* El directorio **data/batches/** contiene código de ejemplo para el modo batch de Livy. Está montado en el nodo donde se ejecuta Livy. Puedes guardar allí tu propio código, o utilizar el directorio universal **data/**.

* El directorio **zeppelin\_notebooks/** contiene, como era de esperar, los archivos de cuadernos de Zeppelin. Gracias a esto, todos tus notebooks persisten entre ejecuciones.

El puerto JDBC de Hive está expuesto al host:

* URI: `jdbc:hive2://localhost:10000`
* Driver: `org.apache.hive.jdbc.HiveDriver` (org.apache.hive\:hive-jdbc:3.1.2)
* Usuario y contraseña: no utilizados.


Si se desea bajar todos los servicios usar:

``` bash
docker-compose down
```

------------------------------------------------------------------------

## Verificación de servicios

### Hadoop y YARN

Revisa la [interfaz web de YARN (Hadoop ResourceManager) (localhost:8088)](http://localhost:8088/).
Deberías ver 2 nodos activos allí.
También existe una [interfaz web alternativa de YARN (http://localhost:8088/ui2)](http://localhost:8088/ui2).

Luego, abre la [interfaz web de Hadoop NameNode (localhost:9870)](http://localhost:9870),
y las interfaces web de Hadoop DataNode en
[http://localhost:9864](http://localhost:9864) y [http://localhost:9865](http://localhost:9865).
Todas esas URLs deberían mostrar una página.

Abre una terminal en el nodo maestro:

```bash
docker-compose exec master bash
jps
```

El comando `jps` muestra una lista de procesos Java en ejecución,
que en un nodo Hadoop NameNode/Spark Master debería incluir:

<pre>
123 Jps
456 ResourceManager
789 NameNode
234 SecondaryNameNode
567 HistoryServer
890 Master
</pre>

aunque no necesariamente en ese orden ni con esos IDs. También pueden aparecer procesos adicionales como `RunJar` o `JobHistoryServer`.

Después, comprobemos si YARN puede ver todos los recursos disponibles (2 nodos worker):

```bash
yarn node -list
```

<pre>
current-datetime INFO client.RMProxy: Connecting to ResourceManager at master/172.28.1.1:8032
Total Nodes:2
         Node-Id	     Node-State	Node-Http-Address	Number-of-Running-Containers
   worker1:45019	        RUNNING	     worker1:8042	                           0
   worker2:41001	        RUNNING	     worker2:8042	                           0
</pre>

Estado de HDFS (Hadoop Distributed File System):

```bash
hdfs dfsadmin -report
```

<pre>
Live datanodes (2):
Name: 172.28.1.2:9866 (worker1)
...
Name: 172.28.1.3:9866 (worker2)
</pre>

Ahora subiremos un archivo a HDFS y verificaremos que sea visible desde todos los nodos:

```bash
hadoop fs -put /data/notas.csv /
hadoop fs -ls /
```

<pre>
Found N items
...
-rw-r--r--   2 root supergroup  ... /notas.csv
...
</pre>

Sal de la sesión del nodo maestro con `Ctrl+D`. Repite el proceso en los demás nodos (hay 3 en total: master, worker1 y worker2):

```bash
docker-compose exec worker1 bash
hadoop fs -ls /
```

<pre>
Found 1 items
-rw-r--r--   2 root supergroup  ... /grades.csv
</pre>

Cuando estamos en los nodos distintos a Hadoop NameNode/Spark Master, la salida del comando `jps` debería mostrar ahora **DataNode** y **Worker**, en lugar de **NameNode** y **Master**:

```bash
jps
```

<pre>
123 Jps
456 NodeManager
789 DataNode
234 Worker
</pre>  

---


### Hive

Ejemplo de creación de tabla y carga de datos desde HDFS.

**Prerrequisito:** debe existir un archivo `notas.csv` almacenado en HDFS (`hadoop fs -put /data/notas.csv /`).

```bash
docker-compose exec master bash
hive
```

```sql
CREATE TABLE notas(
    `Apellido` STRING,
    `Nombre` STRING,
    `Identificacion` STRING,
    `Test1` DOUBLE,
    `Test2` INT,
    `Test3` DOUBLE,
    `Test4` DOUBLE,
    `Final` DOUBLE,
    `Nota` STRING)
COMMENT 'https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
tblproperties("skip.header.line.count"="1");

LOAD DATA INPATH '/notas.csv' INTO TABLE notas;

SELECT * FROM notas;
-- OK
-- Alfalfa	Aloysius	123-45-6789	40.0	90	100.0	83.0	49.0	D-
-- Alfred	University	123-12-1234	41.0	97	96.0	97.0	48.0	D+
-- Gerty	Gramma	567-89-0123	41.0	80	60.0	40.0	44.0	C
-- Android	Electric	087-65-4321	42.0	23	36.0	45.0	47.0	B-
-- Bumpkin	Fred	456-78-9012	43.0	78	88.0	77.0	45.0	A-
-- Rubble	Betty	234-56-7890	44.0	90	80.0	90.0	46.0	C-
-- Noshow	Cecil	345-67-8901	45.0	11	-1.0	4.0	43.0	F
-- Buff	Bif	632-79-9939	46.0	20	30.0	40.0	50.0	B+
-- Airpump	Andrew	223-45-6789	49.0	1	90.0	100.0	83.0	A
-- Backus	Jim	143-12-1234	48.0	1	97.0	96.0	97.0	A+
-- Carnivore	Art	565-89-0123	44.0	1	80.0	60.0	40.0	D+
-- Dandy	Jim	087-75-4321	47.0	1	23.0	36.0	45.0	C+
-- Elephant	Ima	456-71-9012	45.0	1	78.0	88.0	77.0	B-
-- Franklin	Benny	234-56-2890	50.0	1	90.0	80.0	90.0	B-
-- George	Boy	345-67-3901	40.0	1	11.0	-1.0	4.0	B
-- Heffalump	Harvey	632-79-9439	30.0	1	20.0	30.0	40.0	C
-- Time taken: 3.324 seconds, Fetched: 16 row(s)
```

Vuelve a bash con `Ctrl+D`. Verifica si el archivo se cargó en el directorio de Hive warehouse:

```bash
hadoop fs -ls /usr/hive/warehouse/notas
```

<pre>
Found 1 items
-rw-r--r--   2 root supergroup  ... /usr/hive/warehouse/notas/notas.csv
</pre>

La tabla que acabamos de crear debería ser accesible desde todos los nodos. Vamos a verificarlo:

```bash
docker-compose exec worker2 bash
hive
```

```sql
SELECT * FROM notas;
```

Deberías poder ver la misma tabla. ✅


### Spark

Abre la [interfaz web de Spark Master (localhost:8080)](http://localhost:8080/):

<pre>
Workers (2)
Worker Id	Address	State	Cores	Memory
worker-timestamp-172.28.1.3-8882	172.28.1.3:8882	ALIVE	2 (0 Used)	1024.0 MB (0.0 B Used)
worker-timestamp-172.28.1.2-8881	172.28.1.2:8881	ALIVE	2 (0 Used)	1024.0 MB (0.0 B Used)
</pre>

También están las interfaces web de los workers en [localhost:8081](http://localhost:8081/) y [localhost:8082](http://localhost:8082/). Todas esas páginas deberían ser accesibles.

Además, existe el **Spark History Server** ejecutándose en [localhost:18080](http://localhost:18080/). Cada vez que corras trabajos de Spark, podrás verlos allí.

El History Server también incluye una **API REST** en
[localhost:18080/api/v1/applications](http://localhost:18080/api/v1/applications). Es un espejo de todo lo que aparece en la página principal, pero en formato JSON.

---

### Ejecutar trabajos de ejemplo

```bash
docker-compose exec master bash
run-example SparkPi 10
```

O usando `spark-submit`:

```bash
spark-submit --class org.apache.spark.examples.SparkPi \
    --master yarn \
    --deploy-mode client \
    --driver-memory 2g \
    --executor-memory 1g \
    --executor-cores 1 \
    $SPARK_HOME/examples/jars/spark-examples*.jar \
    10
```

Salida esperada:

<pre>
INFO spark.SparkContext: Running Spark version 2.4.4
INFO spark.SparkContext: Submitted application: Spark Pi
..
INFO client.RMProxy: Connecting to ResourceManager at master/172.28.1.1:8032
INFO yarn.Client: Requesting a new application from cluster with 2 NodeManagers
...
INFO yarn.Client: Application report for application_1567375394688_0001 (state: ACCEPTED)
...
INFO yarn.Client: Application report for application_1567375394688_0001 (state: RUNNING)
...
INFO scheduler.DAGScheduler: Job 0 finished: reduce at SparkPi.scala:38, took 1.102882 s
Pi is roughly 3.138915138915139
...
INFO util.ShutdownHookManager: Deleting directory /tmp/spark-81ea2c22-d96e-4d7c-a8d7-9240d8eb22ce
</pre>

---

### Consolas interactivas de Spark

Spark cuenta con 3 shells interactivos:

* **spark-shell** (Scala)
* **pyspark** (Python)
* **sparkR** (R)

Probémoslas todas:

```bash
hadoop fs -put /data/notas.csv /
spark-shell
```

```scala
spark.range(1000 * 1000 * 1000).count()

val df = spark.read.format("csv").option("header", "true").load("/notas.csv")
df.show()

df.createOrReplaceTempView("df")
spark.sql("SHOW TABLES").show()
spark.sql("SELECT * FROM df WHERE Final > 50").show()
```

Salida esperada:

<pre>
Spark context Web UI available at http://localhost:4040
Spark context available as 'sc' (master = yarn, app id = application_N).
Spark session available as 'spark'.

res0: Long = 1000000000

df: org.apache.spark.sql.DataFrame = [Apellido: string, Nombre: string ... 7 more fields]

+---------+----------+-----------+-----+-----+-----+-----+-----+-----+
|Apellido|Nombre|Identificacion|Test1|Test2|Test3|Test4|Final|Nota|
+---------+----------+-----------+-----+-----+-----+-----+-----+-----+
|  Alfalfa|  Aloysius|123-45-6789|   40|   90|  100|   83|   49|   D-|
...
|Heffalump|    Harvey|632-79-9439|   30|    1|   20|   30|   40|    C|
+---------+----------+-----------+-----+-----+-----+-----+-----+-----+
</pre>

---

#### PySpark

```bash
pyspark
```

```python
spark.range(1000 * 1000 * 1000).count()

df = spark.read.format('csv').option('header', 'true').load('/notas.csv')
df.show()

df.createOrReplaceTempView('df')
spark.sql('SHOW TABLES').show()
spark.sql('SELECT * FROM df WHERE Final > 50').show()

# TODO: SELECT TABLE desde Hive - aún no funciona.
spark.sql('SELECT * FROM notas').show()
```

Salida esperada:

<pre>
1000000000
La misma tabla previa
</pre>

---

#### SparkR

```bash
sparkR
```

```R
df <- as.DataFrame(list("Uno", "Dos", "Tres", "Cuatro"), "Esto es un ejemplo")
head(df)

df <- read.df("/notas.csv", "csv", header="true")
head(df)
```

Salida esperada:

<pre>
  Esto es un ejemplo
1                Uno
2                Dos
3               Tres
4             Cuatro

La misma tabla previa
</pre>

---

### Zeppelin

Interfaz en <http://localhost:8890>.

Encontrarás un cuaderno llamado "test" allí, que contiene comandos para probar la integración con bash, Spark y Livy.

### Livy

Livy está disponible en [http://localhost:8998](http://localhost:8998) (y sí, en ese puerto hay tanto una interfaz web como una API REST; basta con hacer clic en el enlace).

### Sesiones de Livy

Probar la API REST:

```bash
curl --request GET \
  --url http://localhost:8998/sessions | python3 -mjson.tool
```

La respuesta, asumiendo que no creaste ninguna sesión antes, debería verse así:

```json
{
  "from": 0,
  "total": 0,
  "sessions": []
}
```

**1) Crear una sesión:**

```bash
curl --request POST \
  --url http://localhost:8998/sessions \
  --header 'content-type: application/json' \
  --data '{
	"kind": "pyspark"
}' | python3 -mjson.tool
```

Respuesta:

```json
{
    "id": 0,
    "name": null,
    "appId": null,
    "owner": null,
    "proxyUser": null,
    "state": "starting",
    "kind": "pyspark",
    "appInfo": {
        "driverLogUrl": null,
        "sparkUiUrl": null
    },
    "log": [
        "stdout: ",
        "\nstderr: ",
        "\nYARN Diagnostics: "
    ]
}
```

**2) Esperar a que la sesión inicie** (el estado cambiará de `"starting"` a `"idle"`):

```bash
curl --request GET \
  --url http://localhost:8998/sessions/0 | python3 -mjson.tool
```

Respuesta:

```json
{
    "id": 0,
    "name": null,
    "appId": "application_1584274334558_0001",
    "owner": null,
    "proxyUser": null,
    "state": "starting",
    "kind": "pyspark",
    "appInfo": {
        "driverLogUrl": "http://worker2:8042/node/containerlogs/container_1584274334558_0003_01_000001/root",
        "sparkUiUrl": "http://master:8088/proxy/application_1584274334558_0003/"
    },
    "log": [
        "timestamp bla"
    ]
}
```

**3) Enviar algunas sentencias:**

```bash
curl --request POST \
  --url http://localhost:8998/sessions/0/statements \
  --header 'content-type: application/json' \
  --data '{
	"code": "import sys;print(sys.version)"
}' | python3 -mjson.tool

curl --request POST \
  --url http://localhost:8998/sessions/0/statements \
  --header 'content-type: application/json' \
  --data '{
	"code": "spark.range(1000 * 1000 * 1000).count()"
}' | python3 -mjson.tool
```

Respuesta:

```json
{
    "id": 0,
    "code": "import sys;print(sys.version)",
    "state": "waiting",
    "output": null,
    "progress": 0.0,
    "started": 0,
    "completed": 0
}
```
```json
{
    "id": 1,
    "code": "spark.range(1000 * 1000 * 1000).count()",
    "state": "waiting",
    "output": null,
    "progress": 0.0,
    "started": 0,
    "completed": 0
}
```

**4) Obtener el resultado:**

```bash
curl --request GET \
  --url http://localhost:8998/sessions/0/statements | python3 -mjson.tool
```

Respuesta:

```json
{
  "total_statements": 2,
  "statements": [
    {
      "id": 0,
      "code": "import sys;print(sys.version)",
      "state": "available",
      "output": {
        "status": "ok",
        "execution_count": 0,
        "data": {
          "text/plain": "3.7.3 (default, Apr  3 2019, 19:16:38) \n[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]]"
        }
      },
      "progress": 1.0
    },
    {
      "id": 1,
      "code": "spark.range(1000 * 1000 * 1000).count()",
      "state": "available",
      "output": {
        "status": "ok",
        "execution_count": 1,
        "data": {
          "text/plain": "1000000000"
        }
      },
      "progress": 1.0
    }
  ]
}
```

**5) Eliminar la sesión:**

```bash
curl --request DELETE \
  --url http://localhost:8998/sessions/0 | python3 -mjson.tool
```

Respuesta:

```json
{
  "msg": "deleted"
}
```

---

### Procesamiento en lotes con Livy (Livy Batches)

**Consultar todos los lotes activos:**

```bash
curl --request GET \
  --url http://localhost:8998/batches | python3 -mjson.tool
```

(Sorprendentemente, esto devuelve una respuesta similar a la de consultar sesiones).

**1) Enviar un lote (batch):**

```bash
curl --request POST \
  --url http://localhost:8998/batches \
  --header 'content-type: application/json' \
  --data '{
	"file": "local:/data/batches/sample_batch.py",
	"pyFiles": ["local:/data/batches/sample_batch.py"],
	"args": ["123"]
}' | python3 -mjson.tool
```

Respuesta:

```json
{
    "id": 0,
    "name": null,
    "owner": null,
    "proxyUser": null,
    "state": "starting",
    "appId": null,
    "appInfo": {
        "driverLogUrl": null,
        "sparkUiUrl": null
    },
    "log": [
        "stdout: ",
        "\nstderr: ",
        "\nYARN Diagnostics: "
    ]
}
```

**2) Consultar el estado:**

```bash
curl --request GET \
  --url http://localhost:8998/batches/0 | python3 -mjson.tool
```

Ejemplo de respuesta:

```json
{
    "id": 0,
    "name": null,
    "owner": null,
    "proxyUser": null,
    "state": "running",
    "appId": "application_1584274334558_0005",
    "appInfo": {
        "driverLogUrl": "http://worker2:8042/node/containerlogs/container_1584274334558_0005_01_000001/root",
        "sparkUiUrl": "http://master:8088/proxy/application_1584274334558_0005/"
    },
    "log": [
        "timestamp bla",
        "\nstderr: ",
        "\nYARN Diagnostics: "
    ]
}
```

**3) Consultar los logs** con el endpoint `/log`:

```bash
curl --request GET \
  --url 'http://localhost:8998/batches/0/log?from=100&to=200' | python3 -mjson.tool
```

Respuesta:

```json
{
    "id": 0,
    "from": 100,
    "total": 203,
    "log": [
        "...",
        "Welcome to",
        "      ____              __",
        "     / __/__  ___ _____/ /__",
        "    _\\ \\/ _ \\/ _ `/ __/  '_/",
        "   /__ / .__/\\_,_/_/ /_/\\_\\   version 2.4.5",
        "      /_/",
        "",
        "Using Python version 3.7.5 (default, Oct 17 2019 12:25:15)",
        "SparkSession available as 'spark'.",
        "3.7.5 (default, Oct 17 2019, 12:25:15) ",
        "[GCC 8.3.0]",
        "Arguments: ",
        "['/data/batches/sample_batch.py', '123']",
        "Custom number passed in args: 123",
        "Will raise 123 to the power of 3...",
        "...",
        "123 ^ 3 = 1860867",
        "...",
        "2020-03-15 13:06:09,503 INFO util.ShutdownHookManager: Deleting directory /tmp/spark-138164b7-c5dc-4dc5-be6b-7a49c6bcdff0/pyspark-4d73b7c7-e27c-462f-9e5a-96011790d059"
    ]
}
```

**4) Eliminar el lote:**

```bash
curl --request DELETE \
  --url http://localhost:8998/batches/0 | python3 -mjson.tool
```

Respuesta:

```json
{
  "msg": "deleted"
}
```

---



