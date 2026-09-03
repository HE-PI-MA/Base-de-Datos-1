# Tarea 5 — Arquitectura de un SGBD

## Enunciado

Se presenta la siguiente arquitectura:

```text
Aplicación Web   App Móvil   Reporte Python
      |               |             |
      +---------------+-------------+
                      |
               ¿Componente X?
                      |
                 Base de Datos
```

Se debe identificar el Componente X, explicar sus funciones, mencionar funciones adicionales de un SGBD y comparar un SGBD con un sistema de archivos.

## a) ¿Qué es el Componente X?

El Componente X representa al Sistema Gestor de Bases de Datos, también denominado SGBD o DBMS.

El SGBD actúa como intermediario entre las aplicaciones y la base de datos.

Las aplicaciones no necesitan acceder directamente a los archivos físicos donde se almacenan los datos.

En su lugar, realizan consultas y operaciones mediante el SGBD.

### Representación

```text
Aplicación Web
       |
App Móvil
       |
Reporte Python
       |
       v
+--------------------------+
|          SGBD            |
|  MySQL / PostgreSQL /    |
|         SQLite           |
+--------------------------+
       |
       v
+--------------------------+
|      Base de Datos       |
+--------------------------+
```

### Funciones principales del Componente X

El SGBD recibe las solicitudes de las aplicaciones, interpreta las instrucciones SQL y administra el acceso a los datos.

Entre sus funciones se encuentran:

- Ejecutar consultas SQL.
- Insertar, modificar y eliminar registros.
- Administrar las conexiones de los usuarios.
- Verificar permisos de acceso.
- Mantener la integridad de los datos.
- Controlar el almacenamiento físico.
- Gestionar transacciones.

## b) Cinco funciones de un SGBD además de almacenar datos

### 1. Control de seguridad

Permite definir usuarios, roles y permisos para determinar quién puede consultar o modificar información.

### 2. Control de concurrencia

Permite que varios usuarios trabajen con la base de datos al mismo tiempo evitando conflictos o pérdida de información.

### 3. Gestión de transacciones

Permite agrupar varias operaciones como una sola unidad de trabajo.

Una transacción puede confirmarse mediante COMMIT o deshacerse mediante ROLLBACK.

### 4. Integridad de datos

Permite utilizar restricciones como claves primarias, claves foráneas, UNIQUE, NOT NULL y CHECK.

Estas restricciones ayudan a evitar información inválida o inconsistente.

### 5. Respaldo y recuperación

El SGBD permite realizar copias de seguridad y recuperar los datos cuando ocurre un fallo o pérdida de información.

## c) Diferencia entre un SGBD y un sistema de archivos

### Sistema de archivos

Un sistema de archivos permite almacenar información directamente en archivos como TXT, CSV, JSON, documentos o archivos binarios.

El sistema operativo se encarga principalmente de organizar los archivos y carpetas.

Sin embargo, por sí solo no ofrece todas las funciones especializadas de administración de datos que posee un SGBD.

### SGBD

Un SGBD administra datos de forma estructurada y permite establecer relaciones, restricciones, permisos, transacciones y consultas.

También facilita el acceso simultáneo de múltiples usuarios.

### Comparación

| Característica | SGBD | Sistema de archivos |
|---|---|---|
| Datos estructurados | Sí | Depende del archivo |
| Consultas SQL | Sí | No directamente |
| Relaciones entre datos | Sí | No de forma nativa |
| Control de usuarios | Sí | Limitado a permisos del sistema operativo |
| Transacciones | Sí | No de forma nativa |
| Integridad referencial | Sí | No de forma nativa |
| Concurrencia | Controlada por el SGBD | Más limitada |
| Copias de seguridad | Herramientas especializadas | Copia manual o mediante el sistema operativo |

## ¿En qué se parecen?

Tanto un SGBD como un sistema de archivos permiten almacenar y recuperar información.

Los dos utilizan finalmente algún tipo de almacenamiento físico, como discos duros o unidades SSD.

Además, ambos necesitan mecanismos para localizar y acceder a la información almacenada.

La diferencia principal es que el SGBD agrega una capa especializada de administración, seguridad, integridad, concurrencia y consulta de datos.

## Ejemplo práctico

Una aplicación web puede ejecutar la siguiente consulta:

```sql
SELECT nombre, apellido
FROM ESTUDIANTE
WHERE ci = '7654321';
```

La aplicación envía esta instrucción al SGBD.

El SGBD interpreta la consulta, localiza los datos en el almacenamiento, verifica los permisos y devuelve el resultado a la aplicación.

La aplicación no necesita saber en qué archivo físico o posición del disco se encuentra almacenado el estudiante.

## Conclusión

El SGBD funciona como intermediario entre las aplicaciones y los datos.

Además de almacenar información, se encarga de la seguridad, integridad, concurrencia, transacciones, consultas y recuperación.

Un sistema de archivos permite almacenar información, pero no proporciona por sí solo todas las funciones especializadas que ofrece un Sistema Gestor de Bases de Datos.
