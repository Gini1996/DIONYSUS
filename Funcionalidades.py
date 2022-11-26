import Init as Ini
import Funcionario as Fun
import Estoque as Est
import Compras as Cp
import Reset as Rst
import ExportaDados as Js
import ImportaDados as Id

def MenuFuncoes(liberacaoAcesso):
    if liberacaoAcesso == 'S':
      print("-------------------------------------------------")
      print("+              FUNCIONALIDADES                  +")
      print("-------------------------------------------------")
      print("+              1 - CADASTRAR FUNCIONARIO        +")
      print("+              2 - ESTOQUE                      +")
      print("+              3 - COMPRAR                      +")
      print("+              4 - EXPORTAR DADOS               +")
      print("+              5 - IMPORTAR DADOS               +")
      print("+              6 - RESET                        +")
      print("+              9 - INICIO                       +")
      print("-------------------------------------------------")
      print("+ ESCOLHA A OPCAO DESEJADA                      +")
      print("-------------------------------------------------")   
      ctrlOp = int(input(""))   
      if ctrlOp == 1:
        Fun.OpcoesFuncionario()
      elif ctrlOp == 2:
        Est.OpcoesEstoque()
      elif ctrlOp == 3:
        Cp.OpcoesCompras()
      elif ctrlOp == 4:
        Js.GerarJSONLogin()
        Js.GerarJSONCompra()
        Js.GerarJSONEstoque()
        Js.GerarJSONFuncionarios()
      elif ctrlOp == 5:
        Id.ImportaInfo()
      elif ctrlOp == 6:
         Rst.Reset()
      elif ctrlOp == 9:
         Ini.TelaInicial()
      else:
        print("-------------------------------------------------")
        print("+               CARARCTERE INVALIDO             +")
        print("-------------------------------------------------")
