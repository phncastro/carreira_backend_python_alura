# Contador de cédulas únicas

cem = []
cinquenta = []
vinte = []
dez = []
cinco = []
dois = []

def sacar():
    '''Realiza o saque do usuário
    
    Inputs:
    - Valor a sacar
    
    Outputs:
    - Quantidade de cada nota que foi sacada'''
    try:
        valor_saque = int(input("Digite o valor do saque: R$"))
    except ValueError:
        raise ValueError("Erro: Digite apenas números.")

    if valor_saque < 0:
        print("Erro: O valor deve ser positivo.")
        return
    
    if valor_saque % 2 != 0:
        print("Erro: O valor deve ser múltiplo de 2.")
        return
    
    while True:
        if valor_saque > 100:
            valor_saque -= 100
            cem.append(100)
        elif valor_saque > 50 and valor_saque < 100:
            valor_saque -= 50
            cinquenta.append(50)
        elif valor_saque > 20 and valor_saque < 50:
            valor_saque -= 20
            vinte.append(20)
        elif valor_saque > 10 and valor_saque < 20:
            valor_saque -= 10
            dez.append(10)
        elif valor_saque > 5 and valor_saque < 10:
            valor_saque -= 5
            cinco.append(5)
        elif valor_saque > 2 and valor_saque < 5:
            valor_saque -= 2
            dois.append(2)
        else:
            break

    print("Cédulas entregues: \n" 
        f"{len(cem)} de R$ 100\n"
        f"{len(cinquenta)} de R$ 50\n"
        f"{len(vinte)} de R$ 20\n"
        f"{len(dez)} de R$ 10\n"
        f"{len(cinco)} de R$ 5\n"
        f"{len(dois)} de R$ 2\n")
    
sacar()

