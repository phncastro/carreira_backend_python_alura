# Gerador de senha segura

import random

def gerador_de_senha():
    '''Gera uma senha de 12 caracteres, contendo pelo menos:
    - 1 caractere especial
    - 1 letra maiúscula
    - 1 letra minúscula
    - 1 número
    '''
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minusculas = letras_maiusculas.lower()
    simbolos = "!@#$%&*"
    numeros = "0123456789"
    todos_caracteres = letras_maiusculas + letras_minusculas + simbolos + numeros

    while True:
        senha = random.sample(todos_caracteres, 12)
        senha_str = "".join(senha)
        if (any(c in letras_maiusculas for c in senha_str) and
            any(c in letras_minusculas for c in senha_str) and
            any(c in simbolos for c in senha_str) and
            any(c in numeros for c in senha_str)):
            break
    print(f"Senha gerada: {senha_str}")

gerador_de_senha()
