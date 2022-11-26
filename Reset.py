import Init as Ini

def Reset():

    temLogin = ''
    validaSenha = ''
    validaAcessoPKLogin = 0000
    validaAcessoPKSenha = 0000
    liberacaoAcesso = ''

    print("------------------------------------------------------")
    print("ATENCAO!! ESTA OPCAO IRA FORMATAR TODA A BASE DE DADOS")
    print(" DESEJA CONTINUAR? S/N ")
    print("------------------------------------------------------")
    ctrlOp = input("")

    if ctrlOp == 'S':
      temLogin = Ini.ValidaUsuario(temLogin,validaAcessoPKLogin)
      validaSenha = Ini.ValidaSenha(validaSenha,validaAcessoPKSenha)
      liberacaoAcesso = Ini.ValidaCredencial(temLogin,validaSenha,liberacaoAcesso)
      if liberacaoAcesso == 'S':
         Ini.DroparTabelas()
         Ini.TelaInicial()
      else:
        print("-------------------------------------------------")
        print("+          USUARIO NAO AUTORIZADO               +")
        print("-------------------------------------------------")
    else:
        print("-------------------------------------------------")
        print("+           Obrigado ate a proxima              +") 
        print("-------------------------------------------------")
        Ini.TelaInicial()
   