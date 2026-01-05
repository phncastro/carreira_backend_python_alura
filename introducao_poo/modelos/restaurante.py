from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    '''Representa um restaurante e suas características.'''
    restaurantes = []

    def __init__(self, nome, categoria):
        '''inicializa uma instância de restaurante.
        
        Paramêtros:
        - nome(str) = Nome do restaurante.
        - categoria(str) = Categoria do restaurante.
        '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        '''Textualiza a vizualização do restaurante em string'''
        return f'{self._nome} | {self.categoria} | {self._avaliacao} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe formatado todos os restaurantes cadastrados e seus dados.'''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        '''Exibe um símbolo demonstrando se o restaurante está ativo ou inativo.
        
        ☒ - Ativo.
        ☐ - Inativo.

        '''
        return '☒' if self._ativo else '☐'
    
    def alternar_estado(self):
        '''Inverte o status atual do restaurante, Ativo/Inativo.'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Recebe uma nota do cliente, entre 1 e 5.

        Paramêtros:
        - cliente(str) = Cliente que registrou a avaliação.
        - nota(float) = Nota dada pelo cliente ao restaurante.        
        '''
        if 0 > nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das notas do restaurante.'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
