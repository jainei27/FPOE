import sqlite3

def save_user():
    try:
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        cedula = int(input("Ingrese la cedula: "))
        correo = input("Ingrese el correo: ")

        conn = sqlite3.connect('Tarea.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO users (nombre, edad, cedula, correo)
        VALUES (?, ?, ?, ?)
        ''', (nombre, edad, cedula, correo))

        conn.commit()
        print("Usuario guardado correctamente.")
    except sqlite3.OperationalError as e:
        print(f"Error de operación en la base de datos: {e}")
    except Exception as e:
        print(f"Error al guardar el usuario: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    save_user()
