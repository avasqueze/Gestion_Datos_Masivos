# Opcional: comandos de conveniencia
up:
	docker compose -f docker/docker-compose.yml up -d
down:
	docker compose -f docker/docker-compose.yml down -v
topics:
	docker compose -f docker/docker-compose.yml exec kafka kafka-topics.sh --create --topic events --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092 || true
hdfs-put:
	docker compose -f docker/docker-compose.yml cp data/clicks_sample.csv namenode:/tmp/clicks_sample.csv && \	docker compose -f docker/docker-compose.yml exec namenode hdfs dfs -mkdir -p /data/raw && \	docker compose -f docker/docker-compose.yml exec namenode hdfs dfs -put -f /tmp/clicks_sample.csv /data/raw/
