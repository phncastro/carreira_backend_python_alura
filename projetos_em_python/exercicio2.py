# Verificando formato de CPF

def validar_cpf():
    '''Função que recebe um CPF e verifica se o formato é válido
    
    Inputs:
    -CPF

    Outputs:
    - Se o CPF é válido ou não
    '''
    try:
        cpf_usuario = input("Digite seu CPF: ")
        cpf_int = int(cpf_usuario)
        if len(cpf_usuario) == 11:
            print("CPF válido")

        if len(cpf_usuario) != 11:
            print("Erro: O CPF deve ter exatamente 11 dígitos.")

    except ValueError:
        print("Erro: O CPF deve conter apenas números.")

validar_cpf()