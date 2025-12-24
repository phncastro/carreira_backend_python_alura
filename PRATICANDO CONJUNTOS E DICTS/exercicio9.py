vendas = { 

    "Eletrônicos": [ 

        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 

        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 

    ], 

    "Eletrodomésticos": [ 

        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 

        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 

    ], 

    "Livros": [ 

        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 

        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 

    ] 

}

def calcula_vendas():
    i = 0
    soma_eletronicos = 0
    soma_eletrodomesticos = 0
    soma_livros = 0 
    for categoria, produtos in vendas.items():
        for produto in produtos:
            multiplica = produto['quantidade'] * produto['valor_unitario']
            if i == 0:
                soma_eletronicos += multiplica
            if i == 1:
                soma_eletrodomesticos += multiplica
            if i == 2:
                soma_livros += multiplica
        i += 1
    
    print('Total de vendas por categoria:')
    print(f'- Eletrônicos: R${soma_eletronicos:.2f}')
    print(f'- Eletrodomésticos: R${soma_eletrodomesticos:.2f}')
    print(f'- Livros: R${soma_livros:.2f}')

calcula_vendas()


