# Introdução a classes - Orientação a Objetos 

class Musica:

    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def lista_musicas():
        for musica in Musica.musicas:
            print(f'Música: {musica.nome} | Artista(s): {musica.artista} | Duração: {musica.duracao} segundos')

musica1 = Musica('Meteoro', 'Luan Santana', '215')
musica2 = Musica('Dubai', 'Hungria', '281')
musica3 = Musica('Anos luz', 'Matuê', '265')

Musica.lista_musicas()


