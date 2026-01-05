from veiculo import Veiculo

class Moto(Veiculo):

    motos = []
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
        self.motos.append(self)

    def __str__(self):
        return f'{super().__str__()} | Tipo: {self.tipo}'