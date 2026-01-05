class Pessoa:

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nProfissao: {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}, e trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'
        
pessoa1 = Pessoa('Pedro', 21, 'Programador')
pessoa2 = Pessoa('Jorge', 30, 'Pedreiro')

print(pessoa2.saudacao)
pessoa1.aniversario()
print(pessoa1)