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

while(controle == True):    
 Ini.TelaInicial()
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
    controle = False
    Ini.EncerraAplicacao()
 else:
    print("Caractere invalido")
