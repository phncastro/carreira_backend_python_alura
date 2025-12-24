produto1_nome = input('Digite o nome do produto: ')
produto1_qtd = int(input('Digite a quantidade: '))

produto2_nome = input('Digite o nome do produto: ')
produto2_qtd = int(input('Digite a quantidade: '))

produto3_nome = input('Digite o nome do produto: ')
produto3_qtd = int(input('Digite a quantidade: '))

produtos = {produto1_nome: produto1_qtd, produto2_nome: produto2_qtd, produto3_nome: produto3_qtd}

print(f'Dicionário de produtos: {produtos}')
