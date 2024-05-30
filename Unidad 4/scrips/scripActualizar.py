import sqlite3

def update_user(user_id):
    conn = sqlite3.connect('Tarea.db')
    cursor = conn.cursor()

    nombre = input("Ingrese el nuevo nombre o presione Enter para mantener el actual: ")
    if nombre:
        cursor.execute('''
        UPDATE users
        SET nombre = ?
        WHERE id = ?
        ''', (nombre, user_id))

    edad = input("Ingrese la nueva edad o presione Enter para mantener la actual: ")
    if edad:
        cursor.execute('''
        UPDATE users
        SET edad = ?
        WHERE id = ?
        ''', (edad, user_id))

    cedula = input("Ingrese la nueva cedula o presione Enter para mantener la actual: ")
    if cedula:
        cursor.execute('''
        UPDATE users
        SET cedula = ?
        WHERE id = ?
        ''', (cedula, user_id))

    correo = input("Ingrese el nuevo correo o presione Enter para mantener la actual: ")
    if correo:
        cursor.execute('''
        UPDATE users
        SET correo = ?
        WHERE id = ?
        ''', (correo, user_id))

    conn.commit()
    conn.close()
    
    print("El usuario ha sido actualizado correctamente.")

# Ejemplo de uso
user_id = int(input("Ingrese el ID del usuario a actualizar: "))
update_user(user_id)
