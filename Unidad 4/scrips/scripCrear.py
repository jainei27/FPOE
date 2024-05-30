import sqlite3

def crear_tabla():
    try:

        conn = sqlite3.connect('Tarea.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            cedula INTEGER NOT NULL,
            correo TEXT NOT NULL UNIQUE
        )
        ''')

        conn.commit()
        print("Tabla 'users' creada o ya existe.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    crear_tabla()
