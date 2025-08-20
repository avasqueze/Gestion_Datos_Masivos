# Guía — Semana 10: Operación Hadoop (fallos y colas YARN)

## Simulación de caída de DataNode
> Solo con fines educativos, no ejecute en entornos productivos.

1) Identifique el contenedor `datanode`:
```bash
docker ps
```
2) Detenga el contenedor por 30s y observe NameNode UI (bloques sub‑replicados):
```bash
docker stop datanode
# ...observar http://localhost:9870 y luego...
docker start datanode
```
3) Revise el *pipeline* de re-réplica desde la UI de NameNode.

## Colas YARN (scheduler)
1) Enviar un job con `spark-submit` (dentro de `resourcemanager`):
```bash
docker compose exec resourcemanager bash
spark-submit --master yarn --deploy-mode client   --conf spark.executor.instances=2   --conf spark.executor.memory=1g   --class org.apache.spark.examples.SparkPi   /opt/spark-examples/jars/spark-examples*.jar 1000
```
