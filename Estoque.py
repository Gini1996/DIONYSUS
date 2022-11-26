import Funcionalidades as Funciona
import BdEstoque as Bd

def OpcoesEstoque():

    ctrl = True
    Acesso = 'S'

    while (ctrl == True):
     print("-------------------------------------------------")
     print("+              ESTOQUE                          +")
     print("-------------------------------------------------")
     print("+              1 - CADASTRAR ESTOQUE            +")
     print("+              2 - VISUALIZAR ESTOQUE           +")
     print("+              3 - EXCLUIR ESTOQUE              +")
     print("+              9 - VOLTAR                       +")
     print("-------------------------------------------------")
     print("+ ESCOLHA A OPCAO DESEJADA                      +")
     print("-------------------------------------------------")

     opcaoFunc = int(input(""))
 
     if opcaoFunc == 1:
       Bd.InserirEstoque()
     elif opcaoFunc == 2:
       Bd.VisualizaEstoque()
     elif opcaoFunc == 3:
       Bd.DeletaEstoque()
     elif opcaoFunc == 9:
       ctrl = False
       Funciona.MenuFuncoes(Acesso)
     else:
         print("-------------------------------------------------")
         print("+               OPCAO INVALIDA                  +")
         print("-------------------------------------------------")