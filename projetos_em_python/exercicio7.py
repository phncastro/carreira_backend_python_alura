# Jogo de adivinhar o número de 1 a 100

import random

numero_gerado = random.randint(1, 100)
def adivinhe_o_numero():
    '''Gera um número de 1 a 100 e pede ao usúario que adivinhe,
    só para a execução quando acerta o número.
    '''
    while True:
        try:
            tentativa = int(input("Tente adivinhar o número (1-100): "))
        except ValueError:
            print(f"Entrada inválida, tente novamente!\n")
            continue
        if tentativa > 0 and tentativa < numero_gerado:
            print(f"Muito baixo! Tente novamente: {tentativa}\n")
            continue
        elif tentativa > numero_gerado and tentativa <= 100:
            print(f"Muito alto! Tente novamente: {tentativa}\n")
            continue
        elif tentativa == numero_gerado:
            print(f"Parabéns! Você acertou o número {numero_gerado}.")
            break
        else:
            print("Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.\n")
            continue

adivinhe_o_numero()