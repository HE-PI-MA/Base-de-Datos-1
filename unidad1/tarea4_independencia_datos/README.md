# Tarea 4 — Independencia de datos

## Enunciado

La base de datos de una universidad tiene inicialmente la siguiente tabla:

```text
ESTUDIANTE(ci, nombre, apellido, fecha_nac)
```

Posteriormente se decide modificarla para agregar el atributo `email` y reemplazar `fecha_nac` por `edad`.

La nueva estructura sería aproximadamente:

```text
ESTUDIANTE(ci, nombre, apellido, edad, email)
```

## a) ¿Qué aplicaciones podrían romperse con este cambio? ¿Por qué?

Podrían verse afectadas todas las aplicaciones que dependan directamente de la estructura anterior de la tabla ESTUDIANTE.

### 1. Aplicaciones que consultan fecha_nac

Una consulta como:

```sql
SELECT ci, nombre, apellido, fecha_nac
FROM ESTUDIANTE;
```

dejaría de funcionar porque la columna `fecha_nac` ya no existiría.

Por ejemplo, podría aparecer un error similar a:

```text
no such column: fecha_nac
```

### 2. Reportes que calculan la edad desde la fecha de nacimiento

Un reporte puede utilizar `fecha_nac` para calcular la edad del estudiante.

Al eliminar esa columna, el reporte tendría que modificarse para trabajar con el nuevo atributo `edad`.

### 3. Aplicaciones que utilizan SELECT *

Una aplicación que utilice:

```sql
SELECT * FROM ESTUDIANTE;
```

puede verse afectada porque ahora recibirá una estructura diferente y una columna adicional llamada `email`.

Si el programa depende de la posición o cantidad exacta de las columnas, puede producir errores.

### 4. Formularios de registro y actualización

Los formularios que solicitaban la fecha de nacimiento deberán cambiar para solicitar o manejar la edad.

Además, deberán adaptarse para permitir registrar el nuevo correo electrónico.

### 5. Sentencias INSERT dependientes de la estructura

Una instrucción escrita sin especificar las columnas puede dejar de funcionar después de agregar una nueva columna.

Por ejemplo:

```sql
INSERT INTO ESTUDIANTE
VALUES ('1234567', 'Ana', 'García', '2001-05-10');
```

Es más seguro indicar explícitamente las columnas utilizadas.

## Observación sobre fecha_nac y edad

Guardar la fecha de nacimiento suele ser más conveniente que almacenar solamente la edad.

La edad cambia con el paso del tiempo, mientras que la fecha de nacimiento permanece constante y permite calcular la edad cuando sea necesario.

Por esta razón, en un sistema real normalmente sería preferible conservar `fecha_nac` y calcular `edad` a partir de ella.

## b) Diferencia entre independencia lógica e independencia física

### Independencia lógica de datos

Es la capacidad de modificar el esquema conceptual de la base de datos sin tener que modificar necesariamente las aplicaciones o vistas utilizadas por los usuarios.

Por ejemplo:

- Agregar una columna.
- Dividir una tabla en varias tablas.
- Crear nuevas relaciones.
- Cambiar algunos atributos manteniendo una interfaz compatible.

En este ejercicio, agregar `email` o modificar la estructura de ESTUDIANTE corresponde a un cambio en el nivel lógico.

### Independencia física de datos

Es la capacidad de modificar la forma en que los datos se almacenan físicamente sin cambiar el esquema lógico ni las aplicaciones.

Por ejemplo:

- Crear o eliminar índices.
- Cambiar la organización física de los archivos.
- Mover la base de datos a otro disco.
- Modificar páginas o estructuras de almacenamiento.

Una aplicación puede seguir ejecutando la misma consulta SQL aunque el SGBD haya cambiado internamente la forma de almacenar los datos.

## c) ¿Cómo ayudan las vistas a mantener la independencia lógica?

Una vista permite presentar a las aplicaciones una estructura estable aunque las tablas internas de la base de datos sufran cambios.

Por ejemplo, si una columna fuera renombrada de `fecha_nac` a `fecha_nacimiento`, se podría crear una vista que mantenga el nombre anterior:

```sql
CREATE VIEW vw_estudiante_compatible AS
SELECT
    ci,
    nombre,
    apellido,
    fecha_nacimiento AS fecha_nac
FROM ESTUDIANTE;
```

De esta manera, una aplicación antigua podría consultar:

```sql
SELECT * FROM vw_estudiante_compatible;
```

y continuar viendo el atributo `fecha_nac`, aunque internamente la tabla haya cambiado.

Las vistas actúan como una capa entre las aplicaciones y la estructura real de las tablas.

Esto reduce la dependencia directa entre los programas y el esquema interno de la base de datos.

### Limitación en el escenario planteado

En el caso específico de reemplazar completamente `fecha_nac` por `edad`, una vista no puede recuperar exactamente la fecha de nacimiento si esa información fue eliminada.

Conocer solamente que una persona tiene, por ejemplo, 20 años no permite determinar con exactitud su día y mes de nacimiento.

Por eso, para mantener compatibilidad completa sería recomendable conservar `fecha_nac` o almacenar esa información en otra estructura.

## Comparación

| Tipo | Qué puede cambiar | Qué debería permanecer estable |
|---|---|---|
| Independencia lógica | Tablas, columnas, relaciones y esquema conceptual | Vistas o programas externos en la medida de lo posible |
| Independencia física | Índices, archivos y organización del almacenamiento | Esquema lógico y aplicaciones |

## Conclusión

La independencia de datos permite reducir el impacto que producen los cambios realizados en una base de datos.

La independencia lógica busca proteger a las aplicaciones frente a modificaciones del esquema conceptual, mientras que la independencia física permite cambiar la forma de almacenamiento sin afectar las consultas ni los programas.

Las vistas son una herramienta importante para mantener una interfaz estable entre las aplicaciones y las tablas de la base de datos.
