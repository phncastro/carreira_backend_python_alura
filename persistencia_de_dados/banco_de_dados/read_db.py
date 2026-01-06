import sqlite3

conn = sqlite3.connect('escola1.db')

cursor = conn.cursor()

cursor.execute(
    '''
        SELECT * FROM estudantes
    '''
)

cursor.execute(
    '''
        SELECT * FROM disciplinas
    '''
)

estudantes = cursor.fetchall()

for estudante in estudantes:
    print(estudante)

disciplinas = cursor.fetchall()

for disciplina in disciplinas:
    print(disciplina)


conn.commit()
conn.close()