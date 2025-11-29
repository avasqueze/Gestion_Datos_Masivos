# Curso de Gestión de Datos Masivos



> **Duración:** 16 semanas · 3 h/semana (36 h)  
> **Requisitos:** Python básico, SQL básico, Linux/CLI básico.  
> **Tecnologías:** Python 3.10+, PySpark 3.x, Hadoop 3.x, Kafka (KRaft), Docker y Docker compose.

## Estructura de carpetas
```
Curso_BigData_12s/
├── docker/                # Docker Compose para Hadoop y Kafka
├── env/                   # Requisitos (pip/conda)
├── slides/                # 12 archivos .md (diapositivas por semana)
├── labs/
│   ├── notebooks/         # Notebooks de PySpark (ipynb)
│   └── guias/             # Instrucciones paso a paso (md)
├── scripts/               # Productor Kafka, utilidades y Makefile opcional
├── data/                  # Datos de ejemplo (CSV/JSONL) + generadores
└── evaluacion/            # Rúbricas y quizzes
```
---

## 📚 Bibliografía recomendada

**Libro principal**

* **“Data Analytics with Hadoop: An Introduction for Data Scientists” (2nd Ed., 2021)** – Benjamin Bengfort, Jenny Kim, Michelle Brush.

  > Muy actualizado en ecosistema Hadoop, Spark, MapReduce y arquitecturas modernas para datos masivos, con ejemplos en Python.

**Libros auxiliares**

1. **“Learning Spark: Lightning-Fast Data Analytics” (2nd Ed., 2020)** – Jules Damji, Brooke Wenig, Tathagata Das, Denny Lee.

   > Guía práctica para Spark 3.x con Python, cubre batch y streaming.
2. **“Fundamentals of Data Engineering” (2022)** – Joe Reis, Matt Housley.

   > Enfoque en arquitectura, ciclo de vida y pipelines de datos a gran escala.
3. **“Streaming Systems: The What, Where, When, and How of Large-Scale Data Processing” (Updated Ed., 2021)** – Tyler Akidau, Slava Chernyak, Reuven Lax.

   > Especializado en procesamiento streaming, arquitecturas Lambda/Kappa.

---

## 📅 Programa del curso – 16 semanas (3 h/semana)

### **Parte 1 – Fundamentos y ciclo de vida (Semanas 1–5)**

| Semana | Tema                                                                      | Actividades/Prácticas                                            |
| ------ | ------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| 1      | Introducción a Big Data, características (3V/5V), casos de uso            | Presentación del curso, instalación de Python y entorno Jupyter. |
| 2      | Datos distribuidos y escalabilidad                                        | Ejercicios con datos particionados en Python.                    |
| 3      | Costos computacionales de almacenamiento y consulta                       | Medición de tiempos y recursos en consultas.                     |
| 4      | Ciclo de vida de datos (adquisición, almacenamiento, análisis, archivado) | Mini-proyecto: documentar un caso real de ciclo de vida.         |
| 5      | Herramientas y entornos de Big Data                                       | Instalación local de Hadoop y Spark (modo standalone).           |

---

### **Parte 2 – Ecosistemas y arquitecturas (Semanas 6–10)**

| Semana | Tema                                                                           | Actividades/Prácticas                   |
| ------ | ------------------------------------------------------------------------------ | --------------------------------------- |
| 6      | Tipos de fuentes de datos: estructurados, no estructurados, semi-estructurados | Ejercicios con CSV, JSON, NoSQL.        |
| 7      | Ingesta y preparación de datos masivos                                         | Uso de PySpark para ETL simple.         |
| 8      | Almacenamiento y flujos de trabajo                                             | Diseño de pipeline básico con Spark.    |
| 9      | Arquitecturas de referencia (simple, Lambda, Kappa)                            | Discusión de casos reales y diagramado. |
| 10     | Ecosistema Hadoop: HDFS, YARN, Hive, Pig                                       | Lectura/escritura en HDFS con Python.   |

---

### **Parte 3 – Procesamiento y arquitecturas avanzadas (Semanas 11–16)**

| Semana | Tema                                      | Actividades/Prácticas                                    |
| ------ | ----------------------------------------- | -------------------------------------------------------- |
| 11     | MapReduce: fundamentos y ejecución        | Implementar WordCount en Hadoop MapReduce y en PySpark.  |
| 12     | Sistemas de datos distribuidos Hadoop     | Pruebas con HDFS y consultas en Hive.                    |
| 13     | Arquitectura Lambda                       | Pipeline batch+streaming con Spark Structured Streaming. |
| 14     | Arquitectura Kappa                        | Pipeline streaming-only con Kafka + Spark.               |
| 15     | Almacenamiento y flujos batch y streaming | Comparativa de rendimiento batch vs streaming.           |
| 16     | Presentación final de proyectos           | Defensa y retroalimentación.                             |

---

## 📊 Evaluación – Proyecto de Aula

* **Entrega 1 (30%, Semana 6)**
  *Diseño del caso de estudio y plan de arquitectura de datos (fuentes, ingesta, almacenamiento, procesamiento).*
* **Entrega 2 (30%, Semana 11)**
  *Implementación parcial: ingesta, almacenamiento y flujo batch con Spark o Hadoop.*
* **Entrega 3 (40%, Semana 16)**
  *Implementación final con arquitectura Lambda o Kappa, incorporando batch y/o streaming, documentación y defensa oral.*

---
