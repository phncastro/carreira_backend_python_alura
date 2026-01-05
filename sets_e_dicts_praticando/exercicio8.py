participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 
removido = input('Nome do participante a ser removido: ')

for grupo in participantes.values():
    for pessoa in grupo.copy():
        if pessoa == removido:
            grupo.remove(pessoa)

        

print('Lista atualizada de participantes:')
print(participantes)
