import sqlite3

def delete_user():
    conn = sqlite3.connect('Tarea.db')
    cursor = conn.cursor()

    user_id = input("Ingrese el ID del usuario que desea eliminar: ")
    cursor.execute('''
    DELETE FROM users
    WHERE id = ?
    ''', (user_id,))

    conn.commit()
    conn.close()

    print("El usuario ha sido eliminado correctamente.")

delete_user()
