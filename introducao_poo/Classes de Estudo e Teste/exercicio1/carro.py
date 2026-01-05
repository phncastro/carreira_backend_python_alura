from veiculo import Veiculo

class Carro(Veiculo):

    carros = []
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
        self.carros.append(self)

    def __str__(self):
        return f'{super().__str__()} | N.º Portas: {self.portas}'