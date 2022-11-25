import psycopg2 as bd

def InserirFuncionario():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     
     print("-------------------------------------------------")
     print("+  Digite o nome do funcionario:                +")
     print("-------------------------------------------------")
     nome = input("")
     print("-------------------------------------------------")
     print("+  Digite o sobrenome do funcionario:           +")
     print("-------------------------------------------------")
     sobrenome = input("")
     print("-------------------------------------------------")
     print("+  Digite o cargo do funcionario:               +")
     print("-------------------------------------------------")
     cargo = input("")
     print("-------------------------------------------------")
     print("+  Digite o mes de admissao do funcionario:     +")
     print("-------------------------------------------------")
     mesAdmissao = int(input(""))
     print("-------------------------------------------------")
     print("+  Digite o ano de admissao do funcionario:     +")
     print("-------------------------------------------------")
     anoAdmissao = int(input(""))
     print("-------------------------------------------------")
     sql = f"INSERT INTO funcionarios (nome,sobrenome,cargo,mesadmissao,anoadmissao) values ('{nome}','{sobrenome}','{cargo}','{mesAdmissao}','{anoAdmissao}') RETURNING nome,sobrenome,cargo,mesadmissao,anoadmissao;"
     cur = con.cursor()
     cur.execute(sql)
     con.commit()
     con.close() 

     print("+        Funcionario Inserido com sucesso!      +")
     print("-------------------------------------------------")
     print("\n")
    except Exception as erro:  
        print("+           Erro ao inserir funcionario         +")
        print("-------------------------------------------------")

def VisualizaFuncionario():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     cursor = con.cursor()
     Qy = "select * from funcionarios"

     cursor.execute(Qy)
     func = cursor.fetchall()
     print("-------------------------------------------------")
     print("+     Lista de funcionarios cadastrados         +")
     print("-------------------------------------------------")
     for row in func:
        print("Id = ", row[0], )
        print("Nome = ", row[1])
        print("Sobrenome = ", row[2])
        print("Cargo = ", row[3])
        print("Mes de Admissao = ", row[4])
        print("Ano de Admissao = ", row[5], "\n")
        print("-------------------------------------------------")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao localizar funcionarios      +")
      print("-------------------------------------------------")

def DeletaFuncionario():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     print("-------------------------------------------------")
     print("+ Digite o Id do funcionario que sera excluido: +")
     print("-------------------------------------------------")
     id = int(input(""))
     sql = f"DELETE FROM funcionarios WHERE idfunc = '{id}';"
     cur = con.cursor()
     cur.execute(sql)
     con.commit()
     con.close() 
     
     print("-------------------------------------------------")
     print("+        Funcionario Excluido com sucesso!      +")
     print("-------------------------------------------------")
     print("\n")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao excluir o funcionario       +")
      print("-------------------------------------------------")