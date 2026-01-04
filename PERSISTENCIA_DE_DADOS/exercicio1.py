""" Na Escola PythonVille, o professor quer registrar as notas dos alunos e depois consultar quem teve um bom desempenho.

Além disso, a coordenação precisa manter um registro organizado com essas informações para uso futuro.

O que você deve fazer:

Crie um programa que grave em um arquivo alunos.csv uma lista de alunos e suas notas.
Leia o arquivo alunos.csv e imprima apenas os alunos com nota maior ou igual a 7.0. """

import csv

alunos_e_notas = [
    ['Joao', 5],
    ['Marcela', 7],
    ['Jessica', 8],
    ['Jonas', 4],
    ['Jose', 10],
]

with open('alunos.csv', 'w', newline= '') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Aluno', 'Nota'])
    escritor.writerows(alunos_e_notas)

with open('alunos.csv', 'r') as f:
    leitor = csv.reader(f)
    next(leitor, None)

    for linha in leitor:
        if int(linha[1]) >= 7:
            print(f'Aluno: {linha[0].ljust(10)} | Nota: {linha[1]}')

