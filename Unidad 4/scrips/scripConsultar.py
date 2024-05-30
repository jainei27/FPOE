import sqlite3

def query_users():
    conn = sqlite3.connect('Tarea.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows

users = query_users()
for user in users:
    print(user)