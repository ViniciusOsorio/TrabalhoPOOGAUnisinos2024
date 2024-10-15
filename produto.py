class Produto:

    #atributos
    __codigo = 0
    __nome = ''
    __preco = 0.0

    #método construtor
    def __init__(self, codigo, nome, preco) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco

    #getters e setters
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, c):
        self.__codigo = c

    @property
    def nome(self):
        return self.__nome
    
    @codigo.setter
    def codigo(self, n):
        self.__nome = n

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, p):
        self.__preco = p