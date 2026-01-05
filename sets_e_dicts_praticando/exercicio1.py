convidados = set()

while True:
    convidado = input('Digite o nome do convidado: ')
    if convidado == 'sair':
        convidados_formatado = ', '.join(str(n) for n in convidados)
        print('Convidados confirmados:',convidados_formatado)
        break
    convidados.add(convidado)
    