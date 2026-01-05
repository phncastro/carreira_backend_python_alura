# Pedra papel ou tesoura

import random
def pedra_papel_tesoura():
    escolha_do_usuario = input("Escolha: pedra, papel ou tesoura? ").lower()
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_da_maquina = random.choice(opcoes)

    print(f"Computador escolheu: {escolha_da_maquina}")
    if escolha_do_usuario == "pedra":
        if escolha_da_maquina == "pedra":
            print("Empate!")
        if escolha_da_maquina == "papel":
            print("Você perdeu!")
        if escolha_da_maquina == "tesoura":
            print("Você ganhou!")

    elif escolha_do_usuario == "papel":
        if escolha_da_maquina == "papel":
            print("Empate!")
        if escolha_da_maquina == "tesoura":
            print("Você perdeu!")
        if escolha_da_maquina == "pedra":
            print("Você ganhou!")

    elif escolha_do_usuario == "tesoura":
        if escolha_da_maquina == "tesoura":
            print("Empate!")
        if escolha_da_maquina == "pedra":
            print("Você perdeu!")
        if escolha_da_maquina == "papel":
            print("Você ganhou!")
    else:
        print("Opção inválida!")

pedra_papel_tesoura()
