import sqlite3

conn = sqlite3.connect('escola1.db')

cursor = conn.cursor()

cursor.execute(
    '''
        UPDATE estudantes SET nome = ?, idade = ? WHERE \
        id = ?
    ''',
    ('Mário', 23, 5)
)

conn.commit()
conn.close()