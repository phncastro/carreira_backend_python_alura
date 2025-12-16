# Gerenciador de tarefas

import os

opcoes_do_menu = ["Adicionar tarefa", "Vizualizar tarefas", "Remover tarefa", "Sair"]
tarefas = []

def limpar_tela():
    '''Função que limpa a tela'''
    os.system("cls")

def exibir_menu():
    '''Função que exibe todas as opções do menu, enumeradas'''
    for numero, opcao in enumerate(opcoes_do_menu):
        print(f"{numero+1}. {opcao}")

def adicionar_tarefa():
    '''Função que adiciona tarefas a lista
    
    Inputs:
    - Tarefa a ser adicionada
    
    Output:
    - Tarefa adicionada a lista'''
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def vizualizar_tarefas():
    '''Função que exibe todas as tarefas enumeradas'''
    print("Tarefas:\n")
    for numero, tarefa in enumerate(tarefas):
        print(f"{numero+1}. {tarefa}")
    print()

def remover_tarefa():
    '''Função que remove uma tarefa da lista
    
    Inputs:
    - Número da tarefa a ser removida
    
    Outputs:
    - Tarefa escolhida é removida da lista'''
    try:
        removida = int(input("Digite o número da tarefa a ser removida: "))
    except ValueError:
        raise ValueError("Erro: Entrada inválida! Digite um número.")
    if not tarefas:
        print("Erro: Nenhuma tarefa para remover.")
    elif removida-1 < 0 or removida-1 > len(tarefas):
        print("Erro: Não existe essa tarefa na lista.")
    else:
        print(f"Tarefa '{tarefas[removida-1]}' removida!")
        del(tarefas[removida-1])

def main():
    '''Recebe todas as outras funções e executa todo o programa'''
    while True:
        exibir_menu()
        try:
            escolha_usuario = int(input("Escolha uma opção: "))
        except ValueError:
            raise ValueError("Erro: Digite apenas números.")
        if escolha_usuario == 1:
            limpar_tela()
            adicionar_tarefa()
        elif escolha_usuario == 2:
            limpar_tela()
            vizualizar_tarefas()
        elif escolha_usuario == 3:
            limpar_tela()
            remover_tarefa()
        elif escolha_usuario == 4:
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")

main()

    
    