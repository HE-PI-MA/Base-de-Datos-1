import sqlite3
from pathlib import Path

# Base de datos de la Tarea 3
DB_PATH = Path(__file__).parent / "universidad_tarea3.db"

# Eliminar una ejecución anterior para obtener siempre el mismo resultado
if DB_PATH.exists():
    DB_PATH.unlink()

conexion = sqlite3.connect(DB_PATH)
cursor = conexion.cursor()

# Crear algunos objetos de ejemplo
cursor.execute("""
CREATE TABLE CARRERA (
    id_carrera INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE ESTUDIANTE (
    ci TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT UNIQUE,
    id_carrera INTEGER,
    FOREIGN KEY (id_carrera) REFERENCES CARRERA(id_carrera)
)
""")

cursor.execute("""
CREATE INDEX idx_estudiante_apellido
ON ESTUDIANTE(apellido)
""")

cursor.execute("""
CREATE VIEW vw_estudiantes AS
SELECT ci, nombre, apellido, email
FROM ESTUDIANTE
""")

conexion.commit()

print("=" * 80)
print("TAREA 3 - METADATOS Y CATALOGO DEL SISTEMA")
print("=" * 80)
print()
print("Consulta ejecutada:")
print("SELECT name, type, sql FROM sqlite_master;")
print()

cursor.execute("SELECT name, type, sql FROM sqlite_master;")
resultados = cursor.fetchall()

for nombre, tipo, sql in resultados:
    print("-" * 80)
    print(f"Nombre : {nombre}")
    print(f"Tipo   : {tipo}")
    print("SQL    :")
    print(sql if sql else "(sin sentencia SQL almacenada)")

print("-" * 80)
print(f"Total de objetos encontrados: {len(resultados)}")
print(f"Base de datos creada en: {DB_PATH}")

conexion.close()
