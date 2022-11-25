import Init as Ini
import Funcionario as Fun

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
        print("AkiOH")
     elif ctrlOp == 3:
        print("AkiOH")
     elif ctrlOp == 4:
        print("AkiOH")
     elif ctrlOp == 5:
        print("AkiOH")
     elif ctrlOp == 6:
        print("AkiOH")
     elif ctrlOp == 9:
        Ini.TelaInicial()
     else:
       print("DeuRuim") 
    else:
        print("-------------------------------------------------")
        print("+               ACESSO RESTRITO                 +")
        print("-------------------------------------------------")
