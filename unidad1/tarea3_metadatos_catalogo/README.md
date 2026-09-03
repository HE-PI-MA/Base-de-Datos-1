# Tarea 3 — Metadatos y catálogo del sistema

## Enunciado

Se debe ejecutar en SQLite la siguiente consulta y analizar el resultado:

```sql
SELECT name, type, sql FROM sqlite_master;
```

## Práctica realizada

Para realizar la práctica se creó una base de datos SQLite llamada `universidad_tarea3.db` mediante Python.

Se crearon los siguientes objetos:

- Tabla CARRERA.
- Tabla ESTUDIANTE.
- Índice idx_estudiante_apellido.
- Vista vw_estudiantes.

Luego se ejecutó la consulta solicitada:

```sql
SELECT name, type, sql FROM sqlite_master;
```

La consulta devolvió un total de 8 objetos.

Entre los resultados obtenidos estuvieron:

| Nombre | Tipo | Descripción |
|---|---|---|
| CARRERA | table | Tabla creada para almacenar carreras |
| sqlite_autoindex_CARRERA_1 | index | Índice automático creado por SQLite |
| sqlite_sequence | table | Tabla interna utilizada por AUTOINCREMENT |
| ESTUDIANTE | table | Tabla creada para almacenar estudiantes |
| sqlite_autoindex_ESTUDIANTE_1 | index | Índice automático de SQLite |
| sqlite_autoindex_ESTUDIANTE_2 | index | Índice automático de SQLite |
| idx_estudiante_apellido | index | Índice creado sobre el apellido del estudiante |
| vw_estudiantes | view | Vista creada para consultar estudiantes |

## a) ¿Qué información devuelve esta consulta?

La consulta devuelve información sobre los objetos que forman la estructura de la base de datos SQLite.

La columna `name` muestra el nombre del objeto.

La columna `type` indica el tipo de objeto, por ejemplo table, index o view.

La columna `sql` muestra la sentencia SQL utilizada para crear el objeto.

Por ejemplo, para la tabla ESTUDIANTE se mostró la sentencia CREATE TABLE completa utilizada para definir sus columnas, claves y restricciones.

También aparecieron objetos creados automáticamente por SQLite.

`sqlite_sequence` apareció porque se utilizó AUTOINCREMENT en la tabla CARRERA.

Los objetos `sqlite_autoindex` fueron creados automáticamente para implementar restricciones como PRIMARY KEY y UNIQUE.

## b) ¿Por qué el catálogo del sistema es en sí mismo una base de datos?

El catálogo del sistema puede considerarse una base de datos porque almacena información estructurada acerca de la propia base de datos.

En lugar de almacenar datos del negocio, almacena metadatos como nombres de tablas, índices, vistas y las instrucciones utilizadas para crearlos.

Además, esta información puede consultarse mediante SQL, de la misma manera que se consultan otras tablas.

En SQLite esta información se encuentra disponible mediante el catálogo `sqlite_master`.

## c) Diferencia entre datos y metadatos

### Datos

Los datos son los valores reales almacenados y utilizados por el sistema.

Ejemplos para una base de datos de estudiantes:

1. CI: 7654321.
2. Nombre: Ana García.
3. Correo: ana.garcia@universidad.edu.

### Metadatos

Los metadatos son información que describe cómo están organizados y definidos los datos.

Ejemplos para una base de datos de estudiantes:

1. La columna `ci` está definida como clave primaria.
2. La columna `nombre` está definida como TEXT y no permite valores nulos.
3. La tabla ESTUDIANTE posee una relación con la tabla CARRERA mediante `id_carrera`.

## Conclusión

La consulta a `sqlite_master` permite conocer la estructura interna de una base de datos SQLite.

La práctica demuestra que un SGBD no solamente almacena los datos de los usuarios, sino también metadatos que describen tablas, índices, vistas, restricciones y otros objetos.

Los datos representan los valores almacenados, mientras que los metadatos describen la estructura y las características de esos datos.
