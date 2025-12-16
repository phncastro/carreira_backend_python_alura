# Calculando a gorjeta de um restaurante 

def calcular_gorjeta():
    '''
    Função que calcula gorjeta

    inputs:
    - Valor da conta
    - Porcentagem da gorjeta

    Outputs:
    - Valor da gorjeta
    - Total a pagar
    '''
    conta = float(input("Digite o valor da conta: "))
    porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: ")) / 100
    gorjeta = conta * porcentagem_gorjeta
    total_a_pagar = conta + gorjeta
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {total_a_pagar:.2f}")

calcular_gorjeta()

