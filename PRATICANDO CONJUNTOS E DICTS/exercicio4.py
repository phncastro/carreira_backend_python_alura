print('> CASO 01:\n')
permissoes_principais = set(input('Permissões principais: ').split(', '))
print()
permissoes_solicitadas = set(input('Permissões solicitadas: ').split(', '))
print()

print('> CASO 02:\n')
permissoes_principais2 = input('Permissões principais: ')
print()
permissoes_solicitadas2 = input('Permissões solicitadas: ')
print()

for item in permissoes_solicitadas:
    

print('As permissões solicitadas fazem parte das permissões principais.')
print('As permissões solicitadas não fazem parte das permissões principais.')