# Ecosistema de Hadoop

Este documento presenta una visión general del **Ecosistema de Hadoop**, un conjunto de herramientas y tecnologías que amplían las capacidades del framework Hadoop en almacenamiento, procesamiento, análisis y gestión de datos a gran escala.

---

## ¿Qué es Hadoop?

**Hadoop** es un framework de código abierto diseñado para almacenar y procesar grandes volúmenes de datos de forma distribuida utilizando hardware común. Su ecosistema agrupa herramientas y tecnologías construidas alrededor de sus componentes centrales —HDFS, YARN, MapReduce y Hadoop Common— para potenciar el almacenamiento, procesamiento, análisis y la gestión de datos.

<p align="center">
<image src="Hadoop-Eco.png" alt="Componentes del ecosistema Hadoop">
</p>

---

## Componentes del Ecosistema de Hadoop

El ecosistema de Hadoop comprende varios componentes que trabajan juntos para permitir un procesamiento eficiente de datos masivos. Los principales son:

### 1. **HDFS (Hadoop Distributed File System)**
Almacena grandes cantidades de datos (estructurados o no) repartidos entre múltiples nodos. Administra metadatos mediante NameNode (nodo maestro) y utiliza DataNodes (nodos de trabajo) para el almacenamiento real.

### 2. **YARN (Yet Another Resource Negotiator)**
Capa de gestión de recursos de Hadoop. Responsable de la programación y asignación de recursos en el clúster.

- **ResourceManager**: asigna recursos a diversas aplicaciones del sistema.
- **NodeManager**: gestiona recursos (CPU, memoria, etc.) en cada nodo y reporta al ResourceManager.
- **ApplicationMaster**: actúa como intermediario entre ResourceManager y NodeManager para cada aplicación. :contentReference[oaicite:2]{index=2}

### 3. **MapReduce**
Modelo de programación para el procesamiento paralelo y distribuido de grandes conjuntos de datos:

- **Map()**: procesa datos de entrada, filtrándolos y organizándolos en pares clave-valor.
- **Reduce()**: toma los resultados de Map, los agrega y resume en un conjunto consolidado de datos.

### 4. **Pig**
Plataforma creada por Yahoo para el análisis de grandes datasets mediante un lenguaje de scripting similar a **SQL** llamado **Pig Latin**. Facilita flujos de datos complejos y ejecuta operaciones MapReduce internamente.

### 5. **Hive**
Proporciona una interfaz similar a SQL (HQL: Hive Query Language) para consultas y manipulación de grandes volúmenes de datos, tanto en tiempo real como por lotes. Incluye:

- Controladores JDBC/ODBC para conexiones y permisos.
- Línea de comandos (CLI) para ejecución de consultas.

### 6. **Mahout**
Biblioteca de aprendizaje automático escalable en Hadoop. Incluye algoritmos para **clustering**, **clasificación** y **filtrado colaborativo**. 

### 7. **Apache Spark**
Plataforma potente para procesamiento por lotes, en tiempo real, interactivo, iterativo y de gráficos. Usa computación **en memoria**, lo que lo hace más rápido y eficiente que los sistemas tradicionales.

### 8. **Apache HBase**
Base de datos **NoSQL** dentro del ecosistema Hadoop, inspirada en Google BigTable. Permite operaciones de lectura/escritura en tiempo real sobre grandes volúmenes de datos de forma eficiente y tolerante a fallos.

---

## Otros Componentes Auxiliares

Además de los principales, el ecosistema incluye otras herramientas importantes:

- **Solr & Lucene**: para búsqueda e indexación de texto; Lucene es la biblioteca Java, mientras que Solr es su plataforma de búsqueda.
- **ZooKeeper**: coordina y sincroniza componentes del clúster, asegurando una comunicación y agrupación consistentes.
- **Oozie**: planificador de flujos de trabajo para tareas Hadoop. Soporta:
  - *Workflow jobs*: trabajos ejecutados en secuencia.
  - *Coordinator jobs*: trabajos disparados por eventos temporales o de datos.
- **Zeppelin** es una herramienta de **notebooks web interactivos** para la exploración y visualización de datos dentro del ecosistema Hadoop. Permite a los usuarios ejecutar código, consultas y visualizaciones en un entorno colaborativo.
- **Apache Livy** es un servicio que actúa como puente entre aplicaciones externas y Apache Spark, permitiendo enviar trabajos, crear sesiones interactivas y consultar resultados mediante una API REST o interfaz web. Facilita la integración de Spark con notebooks como Zeppelin y con otras aplicaciones, sin necesidad de conectarse directamente al clúster.
---

