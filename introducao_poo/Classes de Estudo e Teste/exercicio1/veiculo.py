class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        estado = 'Desligado' if self._ligado == False else 'Ligado'
        return f'Marca: {self.marca.ljust(20)} | Modelo: {self.modelo.ljust(20)} | Estado: {estado.ljust(20)}'
    
    def exibir_veiculos(lista, titulo):
        print(f'{titulo}:\n')
        for veiculo in lista:
            print(veiculo)
        print()

 