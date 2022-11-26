import os
import Init as Ini
import About as Sob
import Funcionalidades as Func

os.system('cls')

controle = True
temLogin = ''
validaSenha = ''
validaAcessoPKLogin = 0000
validaAcessoPKSenha = 0000
liberacaoAcesso = ''

Ini.TelaInicial()

while(controle == True):    
 
 op = int(input(""))

 if(op == 1):
    Ini.ConectaBD()
    Ini.GerarTabelas()

    temLogin = Ini.ValidaUsuario(temLogin,validaAcessoPKLogin)
    validaSenha = Ini.ValidaSenha(validaSenha,validaAcessoPKSenha)
    liberacaoAcesso = Ini.ValidaCredencial(temLogin,validaSenha,liberacaoAcesso)

    Func.MenuFuncoes(liberacaoAcesso)
 elif(op == 2):
    Sob.Sobre()
 elif(op == 9):
    controle = Ini.EncerraAplicacao(controle)
 else:
    print("-------------------------------------------------")
    print("+               CARARCTERE INVALIDO             +")
    print("-------------------------------------------------")


