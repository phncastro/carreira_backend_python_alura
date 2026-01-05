class ContaBancaria:
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular.ljust(17)} | Saldo: {self._saldo}'

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria('Joao', '20.550,30')
ContaBancaria.ativar_conta(conta1)

print(conta1._ativo)

class ContaBancariaPythonica:
    
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
conta2 = ContaBancaria('Maria', '600,00')
print(conta2.titular)

class ClienteBanco:

    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta


conta_cliente1 = ClienteBanco.criar_conta('Marcos', '550')
print(f'Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}') 


    