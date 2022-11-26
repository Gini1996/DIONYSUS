import Funcionalidades as Funciona
import BdCompras as Bd

def OpcoesCompras():

    ctrl = True
    Acesso = 'S'

    while (ctrl == True):
     print("-------------------------------------------------")
     print("+              COMPRAR                          +")
     print("-------------------------------------------------")
     print("+              1 - CADASTRAR COMPRA             +")
     print("+              2 - VISUALIZAR COMPRA            +")
     print("+              3 - EXCLUIR COMPRA               +")
     print("+              9 - VOLTAR                       +")
     print("-------------------------------------------------")
     print("+ ESCOLHA A OPCAO DESEJADA                      +")
     print("-------------------------------------------------")

     opcaoFunc = int(input(""))
 
     if opcaoFunc == 1:
       Bd.InserirCompra()
     elif opcaoFunc == 2:
       Bd.VisualizaCompra()
     elif opcaoFunc == 3:
       Bd.DeletaCompra()
     elif opcaoFunc == 9:
       ctrl = False
       Funciona.MenuFuncoes(Acesso)
     else:
         print("-------------------------------------------------")
         print("+               OPCAO INVALIDA                  +")
         print("-------------------------------------------------")