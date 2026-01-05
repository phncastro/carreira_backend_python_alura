# Calculadora com tratamento de erros

def calculadora():
    '''Função que serve de calculadora
    
    Inputs:
    - número1
    - operador
    - número2

    Outputs:
    - Resultado da operação desejada
    '''
    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Escolha a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        raise ValueError("Erro: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        print("Opção inválida.")

    print(f"\n{num1} {operador} {num2} = {resultado}")

calculadora()