from produto import Produto
import csv

class Pousada:
    
    #atributos
    __nome = ''
    __contato = ''
    __quartos = []
    __reservas = []
    __produtos = []

    #método construtor
    def __init__(self) -> None:
        self.carrega_dados()

    #setters e setters
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def contato(self):
        return self.__contato
    
    @contato.setter
    def contato(self, c):
        self.__contato = c

    @property
    def quartos(self):
        return self.__quartos
    
    @quartos.setter
    def quartos(self, q):
        self.__quartos = q

    @property
    def reservas(self):
        return self.__reservas
    
    @reservas.setter
    def reservas(self, r):
        self.__reservas = r

    @property
    def produtos(self):
        return self.__produtos
    
    @produtos.setter
    def produtos(self, p):
        self.__produtos = p

    #Método para buscar os dados da pousada e atribuí-los aos devidos atributos
    def carrega_dados(self):
        #Abrir o arquivo de texto daa pousada e colocar as informações da mesma nos atributos
        p = open("pousada.txt", "r")
        self.__nome = p.readline().strip()
        self.__contato = p.readline().strip()
        p.close()

        #Abrir o arquivo de texto dos quartos e adicioná-los a um array
        q = open("quartos.txt", "r")
        end_of_line_room = False
        array_qua = []
        while(end_of_line_room != True):
            verif_qua = q.readline()
            if(verif_qua != ""):
                array_qua.append(verif_qua)
            else:
                self.__quartos = array_qua
                end_of_line_room = True
        q.close()

        #Abrir o arquivo de texto das reservas e adicioná-las a um array
        r = open("reservas.txt", "r")
        end_of_line_res = False
        array_res = []
        while(end_of_line_res != True):
            verif_res = r.readline()
            if(verif_res != ""):
                array_res.append(r.readline())
            else:
                self.__reservas = array_res
                end_of_line_res = True
        r.close()

        #Abrir o arquivo de texto dos produtos e adicioná-los a um array
        q = open("produtos.txt", "r")
        end_of_line_prod = False
        array_prod = []
        while(end_of_line_prod != True):
            verif_prod = q.readline().strip()
            if(verif_prod != ""):
                split_prod = verif_prod.split(",")
                w, x, y = split_prod                
                array_prod.append(Produto(w, x, y))
            else:
                self.__produtos = array_prod
                end_of_line_prod = True
        q.close()
    
    def salva_dados():
        return None
    
    def consulta_disponibilidade(self, data, quarto):
        return None
    
    def consulta_reserva():
        return None
    
    def realiza_reserva():
        return None
    
    def cancela_reserva():
        return None
    
    def realiza_checkin():
        return None
    
    def realiza_checkout():
        return None
    
    def teste(self):
        return print("\n",self.__nome,"\n",self.__contato)