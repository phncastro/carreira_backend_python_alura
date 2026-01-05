class Cliente:

    clientes = []

    def __init__(self, nome, idade, cpf, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        Cliente.clientes.append(self)

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nCPF: {self.cpf}\nTelefone: {self.telefone}\n'
    
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'Nome: {cliente.nome}\nIdade: {cliente.idade}\nCPF: {cliente.cpf}\nTelefone: {cliente.telefone}\n')

cliente1 = Cliente('João', '22', '12565437745', '988756743')
cliente2 = Cliente('Felipe', '27', '75671230095', '988490102')
cliente3 = Cliente('Marcelo', '31', '100634470110', '999874501')

Cliente.listar_clientes()