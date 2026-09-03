# Tarea 2 — Archivos vs Base de Datos

## Enunciado

Una biblioteca universitaria lleva el registro de préstamos en archivos de texto planos, uno por día.

Ejemplo:

`prestamos_20240315.txt`

Se debe analizar los problemas que puede generar este método y explicar cómo podrían solucionarse utilizando un SGBD relacional.

## a) Problemas del uso de archivos planos

### 1. Redundancia de información

Los datos de un mismo estudiante o libro pueden repetirse en muchos archivos diferentes.
Por ejemplo, el nombre, código y carrera de un estudiante podrían almacenarse cada vez que realiza un préstamo.

Esto ocupa espacio innecesario y dificulta mantener la información actualizada.

### 2. Inconsistencia de datos

Si los datos de un estudiante cambian, algunos archivos pueden contener la información nueva y otros mantener información antigua.

Por ejemplo, un estudiante podría aparecer con dos números de teléfono diferentes en archivos de distintas fechas.

### 3. Dificultad para realizar búsquedas

Para consultar todos los préstamos realizados por un estudiante sería necesario revisar muchos archivos de texto.

A medida que pasan los meses o años, la cantidad de archivos aumentaría y las consultas serían cada vez más difíciles.

### 4. Problemas de acceso simultáneo

Si dos personas intentan modificar el mismo archivo al mismo tiempo pueden producirse errores o pérdida de información.

Los archivos planos no poseen un sistema avanzado de control de concurrencia.

### 5. Seguridad limitada

Un archivo de texto puede ser abierto, modificado o eliminado fácilmente si una persona tiene acceso a la carpeta.

Es difícil establecer permisos diferentes para administradores, bibliotecarios u otros usuarios.

### 6. Dificultad para realizar respaldos y recuperación

Al existir muchos archivos separados es más difícil garantizar que todos hayan sido respaldados correctamente.

Si un archivo se elimina o se daña, se podría perder el registro completo de los préstamos de ese día.

## b) Solución mediante un SGBD relacional

| Problema | Solución con un SGBD |
|---|---|
| Redundancia | Los datos de estudiantes y libros se almacenan una sola vez y se relacionan mediante claves |
| Inconsistencia | Las actualizaciones se realizan sobre un único registro centralizado |
| Búsquedas difíciles | Se pueden realizar consultas SQL para localizar información rápidamente |
| Acceso simultáneo | El SGBD controla las transacciones y la concurrencia entre usuarios |
| Seguridad limitada | Se pueden crear usuarios, roles y permisos |
| Respaldos | El SGBD dispone de mecanismos para copias de seguridad y recuperación |

## c) ¿Cuándo sería válido utilizar archivos planos?

Los archivos planos pueden ser una buena opción cuando la cantidad de información es pequeña, los datos cambian muy poco y solamente una persona necesita utilizarlos.

Por ejemplo, un archivo de configuración de una aplicación o una lista pequeña que solamente se utilizará una vez puede almacenarse en formato TXT o CSV sin necesidad de instalar un SGBD.

En estos casos, utilizar una base de datos completa podría agregar una complejidad innecesaria.

## Conclusión

Los archivos planos pueden funcionar para almacenar información sencilla y de poca cantidad, pero presentan problemas cuando el volumen de datos y el número de usuarios aumentan.

En una biblioteca universitaria es más conveniente utilizar un SGBD relacional porque permite reducir la redundancia, mantener la consistencia de los datos, realizar consultas rápidamente, controlar el acceso de múltiples usuarios y proteger mejor la información.
