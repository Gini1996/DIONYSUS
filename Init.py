import psycopg2 as bd
import getpass as gp

def TelaInicial():
     print("-------------------------------------------------")
     print("+              BEM-VINDO AO DIONYSUS            +")
     print("-------------------------------------------------")
     print("+              1 - REALIZAR LOGIN               +")
     print("+              2 - SOBRE                        +")
     print("+              9 - SAIR                         +")
     print("-------------------------------------------------")
     print("+ ESCOLHA A OPCAO DESEJADA                      +")
     print("-------------------------------------------------")

def ConectaBD():
    try:
       con = bd.connect(
           database="Dionysus",
           user="postgres",
           password="admin",
           host="localhost",
           port="5432"
       )
       print("-------------------------------------------------")
       print("+             INICIALIZANDO APLICACAO           +")
       print("-------------------------------------------------")
       print("+        Base de Dados conectada com sucesso!   +")

    except Exception as erro:
       print(erro)

def GerarTabelas():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )

     sql = """CREATE TABLE login_sistema
     (
         id serial,
         usuario varchar(10),
         senha varchar(10),
         nome varchar(50),
         sobrenome varchar(50),
         constraint pk_login_sistema primary key(id)
     );"""

     cur = con.cursor()
     cur.execute(sql)
     
     sqlAddAdm = f"INSERT INTO login_sistema (usuario,senha,nome,sobrenome) values ('admin','admin','admin','admin') RETURNING id;"
     curAdd = con.cursor()
     curAdd.execute(sqlAddAdm)
     con.commit()
     print("+           Tabelas Geradas com sucesso!        +")
     print("-------------------------------------------------")
     print("\n")
     
    except Exception as erro:  
     print("+           Tabela e acesso já criados          +")
     print("-------------------------------------------------")

def DroparTabelas():
    try:
     con = bd.connect(
     database="Dionysus",
     user="postgres",
     password="admin",
     host="localhost",
     port="5432"
    )

     drop = """DROP TABLE login_sistema"""
     
     cur = con.cursor()
     cur.execute(drop)
     con.commit()
     print("Tabelas Excluidas com Sucesso!")

    except Exception as erro:
     print("Não existem tabelas para excluir")

def ValidaUsuario(temLogin,validaAcessoPKLogin):
    try:
     con = bd.connect(
     database="Dionysus",
     user="postgres",
     password="admin",
     host="localhost",
     port="5432"
    )
     print("-------------------------------------------------")
     login = input("Digite seu login:\n")

     cur = con.cursor()
     sqlValidaUsr = """SELECT * FROM login_sistema;"""
     
     cur.execute(sqlValidaUsr)
     exists_usr = cur.fetchall()
     
     for row in exists_usr:
      if login == row[1]:
       temLogin = 'S'
       validaAcessoPKLogin = row[0]
      else:
       temLogin = 'N'

    except Exception as erro:
     print("Erro, usuario incorreto")
    finally:
      con.commit()
      return temLogin,validaAcessoPKLogin

def ValidaSenha(senhaValida,validaAcessoPKSenha):
    checaSenha = 0
    tentativa = 1

    try:
     con = bd.connect(
     database="Dionysus",
     user="postgres",
     password="admin",
     host="localhost",
     port="5432"
    )
     while(checaSenha < 3): 
      print("-------------------------------------------------")
      senha = gp.getpass("Digite sua senha:\n")
      cur = con.cursor()
      sqlValidaSenha = """SELECT * FROM login_sistema;"""
     
      cur.execute(sqlValidaSenha)
      exists_pass = cur.fetchall()

      for row in exists_pass:
        if senha == row[2]:
         senhaValida = 'S'
         checaSenha = 10
         validaAcessoPKSenha = row[0]
        else:
          senhaValida = 'N'
          checaSenha = checaSenha + 1   
          print(f"Tentativa: {tentativa} de 3")  
          tentativa = tentativa + 1
    except Exception as erro:
     print("Erro, senha incorreta")
    finally:
        con.commit()
        return senhaValida,validaAcessoPKSenha

def ValidaCredencial(temLogin,validaSenha,liberacaoAcesso):
    if temLogin == validaSenha:
         print("-------------------------------------------------")
         print("+           LOGIN REALIZADO COM SUCESSO         +")
         print("-------------------------------------------------")
         liberacaoAcesso = 'S'
    else:
        print("-------------------------------------------------")
        print("+   ERRO, ENTRE EM CONTATO COM O SUPORTE        +")
        print("-------------------------------------------------")
        liberacaoAcesso = 'N'

    return liberacaoAcesso

def EncerraAplicacao():
    print("-------------------------------------------------")
    print("+           Obrigado ate a proxima              +") 
    print("-------------------------------------------------")
