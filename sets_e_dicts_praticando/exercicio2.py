texto1 = input('Texto 1: ').lower()
texto2 = input('Texto 2: ').lower()

palavras_texto1 = set()
palavras_texto2 = set()

for palavra in texto1.split(' '):
    palavras_texto1.add(palavra)

for palavra in texto2.split(' '):
    palavras_texto2.add(palavra)

palavras_comuns = (palavras_texto1) & (palavras_texto2)
print(f'Palavras em comum: {palavras_comuns}')