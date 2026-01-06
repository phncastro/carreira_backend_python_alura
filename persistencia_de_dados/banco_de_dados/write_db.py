import sqlite3

conn = sqlite3.connect('escola1.db')

cursor = conn.cursor()

""" cursor.execute(
    '''
        INSERT INTO estudantes(nome, idade)
        VALUES(?, ?)
    ''',
    ('Mateus', 19)
) """

cursor.execute(
    '''
        INSERT INTO disciplinas(estudante_id, nome_disciplina)
        VALUES(?, ?)
    ''',
    (1, 'Biologia')
)

conn.commit()
conn.close()