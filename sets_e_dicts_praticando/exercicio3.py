lista_de_laura = set(input('Lista de Laura: ').split(', '))
lista_de_ana = set(input('Lista de Ana: ').split(', '))

ambas = lista_de_laura.intersection(lista_de_ana)
exclusivo_laura = lista_de_laura.difference(lista_de_ana)
exclusivo_ana = lista_de_ana.difference(lista_de_laura)

print(f"Itens em ambas as listas: {', '.join(ambas)}")  

print(f"Itens exclusivos de Laura: {', '.join(exclusivo_laura)}")  

print(f"Itens exclusivos de Ana: {', '.join(exclusivo_ana)}")