# Encontrando palavras longas em um texto
def encontra_palavras_longas():
    '''Encontra palavras com mais de 10 letras
    
    Inputs:
    - Texto

    Outputs:
    - Se tem ou não palavras longas, se sim exibe quais são
    '''
    texto = input("Digite um texto: ")
    palavras = texto.split()
    palavras_longas = [] 
    for palavra in palavras:
        if len(palavra) > 10 :
            palavras_longas.append(palavra)
    if len(palavras_longas) == 0:
        print("Nenhuma palavra longa foi encontrada no texto.")
    else:
        print("Palavras longas encontradas:", ", ".join(palavras_longas))
