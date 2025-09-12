# Guía — Semana 2: HDFS básico (CLI)

Objetivo: familiarizarse con comandos HDFS e interacciones con el NameNode/DataNode.

## Pasos
1) Levante el cluster:
```bash
cd docker && docker compose up -d
```
2) Cree directorios y cargue archivos:
```bash
docker compose exec namenode hdfs dfs -mkdir -p /data/raw
docker compose cp ../data/clicks_sample.csv namenode:/tmp/clicks_sample.csv
docker compose exec namenode hdfs dfs -put -f /tmp/clicks_sample.csv /data/raw/
```
3) Explore y consulte tamaños:
```bash
docker compose exec namenode hdfs dfs -ls -h /data/raw
docker compose exec namenode hdfs dfs -du -h /data/raw
```
