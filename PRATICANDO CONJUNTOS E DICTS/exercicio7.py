participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

} 

nomes = []
idades = []

for nome, idade in participantes.items():
    nomes.append(nome)
    idades.append(idade)

print('Nome dos participantes:', ', '.join(nomes))
print('Idade dos participantes:', ', '.join(map(str, idades)))

print("Participantes e suas idades:")
for nome, idade_participante in participantes.items():
    print(f'- {nome}: {idade_participante} anos')
