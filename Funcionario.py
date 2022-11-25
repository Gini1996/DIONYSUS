import Funcionalidades as Funciona
import BdFuncionario as BdFunc

def OpcoesFuncionario():

    ctrl = True
    Acesso = 'S'

    while (ctrl == True):
     print("-------------------------------------------------")
     print("+              FUNCIONARIOS                     +")
     print("-------------------------------------------------")
     print("+              1 - CADASTRAR FUNCIONARIO        +")
     print("+              2 - VISUALIZAR FUNCIONARIOS      +")
     print("+              3 - EXCLUIR FUNCIONARIO          +")
     print("+              9 - VOLTAR                       +")
     print("-------------------------------------------------")
     print("+ ESCOLHA A OPCAO DESEJADA                      +")
     print("-------------------------------------------------")

     opcaoFunc = int(input(""))
 
     if opcaoFunc == 1:
       BdFunc.InserirFuncionario()
     elif opcaoFunc == 2:
       BdFunc.VisualizaFuncionario()
     elif opcaoFunc == 3:
       BdFunc.DeletaFuncionario()
     elif opcaoFunc == 9:
       ctrl = False
       Funciona.MenuFuncoes(Acesso)
     else:
         print("-------------------------------------------------")
         print("+               OPCAO INVALIDA                  +")
         print("-------------------------------------------------")