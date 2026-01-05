class Livro:

    livros = []
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
    
    def __str__(self):
        return f'Titulo: {self.titulo.ljust(20)} | Autor: {self.autor.ljust(20)} | Ano de publicação: {self.ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis
            


livro1 = Livro('Dora', 'José', 2018)
livro2 = Livro('Amarelinha', 'Pedro', 2001)

print(livro1)
print(livro2)

livro1.emprestar()
print(livro1.disponivel)

Livro.verificar_disponibilidade(2018)