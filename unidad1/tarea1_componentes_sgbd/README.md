# Tarea 1 — Identificación de componentes de un SGBD

## Enunciado

Una empresa de logística maneja envíos, clientes, rutas y conductores.
Los envíos se registran con fecha, origen, destino, peso y estado.

Estados posibles:
- Pendiente
- En ruta
- Entregado

## a) Minimundo y entidades

### Minimundo

Una empresa de logística necesita administrar los envíos que realiza para sus clientes.
Cada envío debe registrar la fecha, origen, destino, peso y estado.
También se debe conocer qué cliente solicita el envío, qué ruta se utiliza y qué conductor es responsable del transporte.

### Entidades principales

| Entidad | Atributos principales |
|---|---|
| CLIENTE | id_cliente, nombre, telefono, direccion |
| ENVIO | id_envio, fecha, origen, destino, peso, estado |
| RUTA | id_ruta, origen, destino, distancia |
| CONDUCTOR | id_conductor, nombre, licencia, telefono |

## b) SGBD seleccionado

Se utilizaría MySQL.

### Justificación

MySQL permite trabajar con bases de datos relacionales y con varios usuarios al mismo tiempo.
Además ofrece claves primarias y foráneas, relaciones entre tablas, consultas SQL, transacciones, usuarios, permisos y copias de seguridad.

### Comparación

| SGBD | Característica |
|---|---|
| SQLite | Adecuado para sistemas pequeños y aplicaciones locales |
| MySQL | Adecuado para sistemas relacionales y multiusuario |
| PostgreSQL | Adecuado para sistemas complejos y de gran capacidad |

Elección final: MySQL.

## c) Actores del sistema

### 1. Administrador

Operaciones:
- Administrar usuarios.
- Registrar conductores.
- Consultar información general.
- Gestionar permisos.
- Consultar reportes.

### 2. Operador de logística

Operaciones:
- Registrar clientes.
- Registrar envíos.
- Asignar rutas.
- Asignar conductores.
- Consultar el estado de los envíos.

### 3. Conductor

Operaciones:
- Consultar sus envíos asignados.
- Consultar la ruta.
- Actualizar el estado del envío.
- Marcar un envío como entregado.

## d) Arquitectura de tres niveles

### Nivel externo

Representa las vistas que utiliza cada tipo de usuario: administrador, operador y conductor.

### Nivel conceptual

Representa la estructura lógica completa de la base de datos, incluyendo CLIENTE, ENVIO, RUTA y CONDUCTOR, además de sus relaciones y restricciones.

### Nivel interno

Representa la forma en que MySQL almacena físicamente los datos mediante archivos, índices y páginas de almacenamiento.

### Representación

```text
NIVEL EXTERNO
  - Vista Administrador
  - Vista Operador
  - Vista Conductor
          |
          v
NIVEL CONCEPTUAL
  - CLIENTE
  - ENVIO
  - RUTA
  - CONDUCTOR
  - Relaciones y restricciones
          |
          v
NIVEL INTERNO
  - MySQL
  - Archivos físicos
  - Índices
  - Páginas de almacenamiento
```

## Conclusión

La empresa de logística puede representarse mediante las entidades CLIENTE, ENVIO, RUTA y CONDUCTOR.
Se selecciona MySQL como SGBD porque permite trabajar con bases de datos relacionales y múltiples usuarios.
Los actores principales son el administrador, el operador de logística y el conductor.
El sistema puede organizarse utilizando los niveles externo, conceptual e interno de la arquitectura ANSI/SPARC.
