# Introducción a Docker, Docker Compose y Docker Hub

------------------------------------------------------------------------

## ¿Qué es Docker?

**Docker** es una plataforma de software que permite crear, probar y desplegar aplicaciones de manera rápida y consistente mediante **contenedores**.

Un contenedor es una unidad que incluye todo lo necesario para ejecutar una aplicación: código, librerías, dependencias y configuraciones, asegurando que se ejecute igual en cualquier entorno.

### Características principales:

-   Portabilidad: "Se ejecuta en mi máquina" deja de ser un problema.
-   Ligereza: Los contenedores comparten el kernel del sistema operativo, lo que los hace más livianos que las máquinas virtuales.
-   Escalabilidad: Ideal para arquitecturas de microservicios.
-   Rapidez: Arranque casi instantáneo.

Ejemplo básico para ejecutar un contenedor:

``` bash
docker run hello-world
```

------------------------------------------------------------------------

## ¿Qué es Docker Compose?

**Docker Compose** es una herramienta que permite definir y ejecutar aplicaciones multi-contenedor usando un solo archivo de configuración (`docker-compose.yml`).

Con Compose puedes levantar servicios relacionados (Hadoop y Spark) con un solo comando.

### Ventajas:

-   Define múltiples servicios en un archivo legible (YAML).
-   Facilita levantar entornos de desarrollo completos con un solo comando.
-   Permite manejar redes, volúmenes y dependencias entre contenedores.

### Partes de un archivo `docker-compose.yml`

Un archivo `docker-compose.yml` se usa para definir y gestionar múltiples contenedores Docker como un solo servicio. Está escrito en formato **YAML** (https://www.datacamp.com/blog/what-is-yaml?utm_source=chatgpt.com) y se compone de varias secciones principales.

------------------------------------------------------------------------

#### 1. **Version**

Define la versión del esquema de Docker Compose que se está utilizando.\
Ejemplo:

``` yaml
version: "3.9"
```

------------------------------------------------------------------------

#### 2. **Services**

Es la sección principal, donde se definen los contenedores (servicios).
Cada servicio representa un contenedor que Docker Compose levantará.\
Dentro de cada servicio se especifican opciones como: - **image**: la
imagen de Docker que se usará. - **build**: instrucciones para construir
la imagen (si no se usa una preexistente). - **ports**: mapeo de puertos
del host al contenedor. - **volumes**: directorios o archivos
compartidos entre host y contenedor. - **environment**: variables de
entorno. - **depends_on**: orden de inicio entre servicios.

Ejemplo:

``` yaml
services:
  web:
    build: .
    ports:
      - "8080:80"
    volumes:
      - .:/app
    environment:
      - DEBUG=true
    depends_on:
      - db

  db:
    image: postgres:14
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
```

------------------------------------------------------------------------

#### 3. **Volumes**

Define volúmenes persistentes que pueden ser compartidos entre
servicios.\
Ejemplo:

``` yaml
volumes:
  db_data:
```

Luego, se pueden usar en un servicio:

``` yaml
services:
  db:
    volumes:
      - db_data:/var/lib/postgresql/data
```

------------------------------------------------------------------------

#### 4. **Networks**

Permite definir redes personalizadas para conectar los contenedores
entre sí.\
Ejemplo:

``` yaml
networks:
  backend:
```

Y en los servicios:

``` yaml
services:
  web:
    networks:
      - backend
```

------------------------------------------------------------------------

#### Resumen visual de la estructura

``` yaml
version: "3.9"
services:
  servicio1:
    image: ...
    build: ...
    ports:
    volumes:
    environment:
    depends_on:
  servicio2:
    image: ...
volumes:
  ...
networks:
  ...
```


Ejecutar con:

``` bash
docker-compose up
```

------------------------------------------------------------------------

## ¿Qué es Docker Hub?

**Docker Hub** es un **registro de imágenes** en la nube, administrado por Docker Inc. Funciona como un repositorio donde los desarrolladores pueden: 
- Descargar imágenes oficiales (nginx, postgres, redis, etc.). 
- Subir sus propias imágenes personalizadas. 
- Compartir y versionar imágenes con equipos o la comunidad.

### Ventajas:

-   Repositorio centralizado de imágenes confiables.
-   Integración directa con Docker CLI.
-   Automatización de builds y despliegues.

Ejemplo para descargar una imagen desde Docker Hub:

``` bash
docker pull nginx:latest
```

------------------------------------------------------------------------

## Resumen

-   **Docker**: plataforma para crear y ejecutar aplicaciones en contenedores.
-   **Docker Compose**: orquestador simple de múltiples contenedores con un archivo YAML.
-   **Docker Hub**: repositorio público/privado de imágenes Docker en la nube.

Juntas, estas herramientas permiten un flujo de trabajo ágil y consistente desde el desarrollo hasta la producción.


