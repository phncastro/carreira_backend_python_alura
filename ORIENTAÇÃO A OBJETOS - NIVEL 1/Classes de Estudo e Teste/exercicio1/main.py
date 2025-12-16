from carro import Carro
from moto import Moto

carro1 = Carro('Volkswagen', 'Golf', 4)
carro2 = Carro('Volkswagen', 'Polo', 4)
carro3 = Carro('Volkswagen', 'Gol', 4)
carro4 = Carro('Volkswagen', 'Jetta', 4)
carro5 = Carro('Volkswagen', 'Passat', 4)
carro6 = Carro('Volkswagen', 'Nivus', 4)
carro7 = Carro('Chevrolet', 'Tracker', 4)
carro8 = Carro('Fiat', 'Punto', 4)
carro9 = Carro('Honda', 'Civic', 4)

moto1 = Moto('Kawasaki', 'Z1000', 'Esportiva')
moto2 = Moto('Honda', 'CG Titan 160', 'Casual')
moto3 = Moto('BMW', 'S1000 RR', 'Esportiva')
moto4 = Moto('Yamaha', 'XJ6', 'Esportiva')

Carro.exibir_veiculos(Carro.carros, 'Carros')
Moto.exibir_veiculos(Moto.motos, 'Motos')
