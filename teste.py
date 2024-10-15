from pousada import Pousada
import os
from datetime import datetime

pousada = Pousada()
oper = 0
fechar_sistema = False
rodar = False
eol = False

#função de limpar tela, para não deixar a tela tão poluída
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

""" f = open("produtos.txt", "r")
while(eol != True):
    linha = f.readline().strip()
    if(linha != ""):
        print(linha)
    else:
        print("Fim")
        eol = True
f.close()
 """
eol = False
c = open("quartos.txt", "r")
while(eol == False):
    teste = c.readline().strip()
    if(teste != ""):
        split_array = teste.split(",")
        print(split_array)
    else:
        eol = True




if(rodar):
    print("\nBem-vindos à" ,pousada.nome,"!\nInforme a operação desejada conforme as opções:\n")

    #While para manter o sistema rodando até que usuário selecione a opção de fechar o sistema
    while(not fechar_sistema):
        oper = input("1- Consultar Disponibilidade de Quarto"
                    +"\n2- Consultar Reserva"
                    +"\n3- Gerar Reserva"
                    +"\n4- Cancelar Reserva"
                    +"\n5- Realizar Check-In"
                    +"\n6- Realizar Check-Out"
                    +"\n7- Registrar Consumo"
                    +"\n8- Salvar Alterações"
                    +"\n0- Encerrar o Sistema"
                    +"\nOpção desejada: ")

    #match para verificar qual a opção que o usuário deseja selecionar
        match(oper):
            case "1":
                limparTela()
                conf_data = input("Informe a data que deseja conferir (Formato: dd/mm/aa): ")            
                conf_quarto = input("\nAgora informe o quarto que deseja verificar: ")
                pousada.consulta_disponibilidade(conf_data, conf_quarto)
                limparTela()
            
            case "2":
                limparTela()
                input("oper2")
                limparTela()

            case "3":
                limparTela()
                input("oper3")
                limparTela()

            case "4":
                limparTela()
                input("oper4")
                limparTela()

            case "5":
                limparTela()
                input("oper5")
                limparTela()

            case "6":
                limparTela()
                input("oper6")
                limparTela()

            case "7":
                limparTela()
                input("oper7")
                limparTela()

            case "8":
                limparTela()
                input("oper8")
                limparTela()

            case "0":
                limparTela()
                fechar_sistema = True
                input("A Pousada Colina Silenciosa agradece a preferência! Um bom descanso e volte sempre.")
                limparTela()