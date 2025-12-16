# Contando a quantidade de vogais
def conta_vogais():
    '''Função que conta a quantidade de vogais de um texto
    
    Inputs:
    - Texto

    Outputs:
    - Quantidade de vogais no texto
    '''
    texto = input("Digite um texto: ").lower()
    todas_vogais = "aáàâãeéêiíoóôõuú"
    vogais = 0
    for letra in texto:
        if letra in todas_vogais:
            vogais += 1
    print(f"O texto contém {vogais} vogais.")

conta_vogais()