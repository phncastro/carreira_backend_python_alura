print('> CASO 01:\n')
permissoes_principais = set(input('Permissões principais: ').split(', '))
print()
permissoes_solicitadas = set(input('Permissões solicitadas: ').split(', '))
print()

print('> CASO 02:\n')
permissoes_principais2 = set(input('Permissões principais: ').split(', '))
print()
permissoes_solicitadas2 = set(input('Permissões solicitadas: ').split(', '))
print()

itens = []
for item in permissoes_solicitadas:
    if item in permissoes_principais:
        itens.append(item)

if len(itens) == len(permissoes_solicitadas):
    print('> CASO 01:\n')
    print('As permissões solicitadas fazem parte das permissões principais.')
    print()
else:
    print('> CASO 01:\n')
    print('As permissões solicitadas não fazem parte das permissões principais.')
    print()

itens2 = []
for item2 in permissoes_solicitadas2:
    if item2 in permissoes_principais2:
        itens2.append(item)

if len(itens2) == len(permissoes_solicitadas2):
    print('> CASO 02:\n')
    print('As permissões solicitadas fazem parte das permissões principais.')
    print()
else:
    print('> CASO 02:\n')
    print('As permissões solicitadas não fazem parte das permissões principais.')
    print()