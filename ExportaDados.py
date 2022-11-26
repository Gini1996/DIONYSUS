import psycopg2 as bd
import json 
import Funcionalidades as Fun
import zipfile as zp

def GerarJSONLogin():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
    )
     cursor = con.cursor()
     QyLogin = "select * from login_sistema"
     cursor.execute(QyLogin)
     arquivo = []

     funcLogin = cursor.fetchall()
     
     for row in funcLogin:
        arquivo.append({'Tabela':'Login_sistema','Id':row[0],'Usuario':row[1],'Senha':row[2],'Nome':row[3],'Sobrenome':row[4]})
        f = open('Exportacao/DadosLogin', 'w')
        json.dump(arquivo, f, sort_keys=True, indent=4)
        f.close()

     z = zp.ZipFile('DadosLogin.zip', 'w', zp.ZIP_DEFLATED)
     z.write('Exportacao/DadosLogin')
     z.close()
    
     print("----------------------------------------------------------")
     print("+      Concluido, arquivo de login gerado com sucesso    +")
     print("----------------------------------------------------------")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao exportar dados                      +")
      print("---------------------------------------------------------")

def GerarJSONCompra():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     cursor = con.cursor()
     QyCompra = "select * from compra"

     cursor.execute(QyCompra)
     
     arquivo = []

     funcCompra = cursor.fetchall()
     for row in funcCompra:
        arquivo.append({'Tabela':'Compra','Id':row[0],'Produto':row[1],'Fornecedor':row[2],'Quantidade':row[3]})
        f = open('Exportacao/DadosCompra', 'w')
        json.dump(arquivo, f, sort_keys=True, indent=4)
        f.close()
  
     z = zp.ZipFile('DadosCompra.zip', 'w', zp.ZIP_DEFLATED)
     z.write('Exportacao/DadosCompra')
     z.close()

     print("-----------------------------------------------------------")
     print("+      Concluido, arquivo de compra gerado com sucesso    +")
     print("-----------------------------------------------------------")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao exportar dados                       +")
      print("----------------------------------------------------------")

def GerarJSONEstoque():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     
     cursor = con.cursor()
     QyEstoque = "select * from estoque"
     cursor.execute(QyEstoque)   
     arquivo = []
 
     funcEstoque = cursor.fetchall()
     for row in funcEstoque:
        arquivo.append({'Tabela':'Estoque','Id':row[0],'Produto':row[1],'Perecivel':row[2],'Quantidade':row[3],'PrecoCusto':row[4],'PrecoVenda':row[5]})
        f = open('Exportacao/DadosEstoque', 'w')
        json.dump(arquivo, f, sort_keys=True, indent=4)
        f.close()

     z = zp.ZipFile('DadosEstoque.zip', 'w', zp.ZIP_DEFLATED)
     z.write('Exportacao/DadosEstoque')
     z.close()

     print("------------------------------------------------------------")
     print("+      Concluido, arquivo de estoque gerado com sucesso    +")
     print("------------------------------------------------------------")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao exportar dados                        +")
      print("-----------------------------------------------------------")

def GerarJSONFuncionarios():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     cursor = con.cursor()
     QyFuncionarios = "select * from funcionarios"
     cursor.execute(QyFuncionarios)

     arquivo = []
 
     funcFuncionarios = cursor.fetchall()
     for row in funcFuncionarios:
        arquivo.append({'Tabela':'Funcionarios','Id':row[0],'Nome':row[1],'Sobrenome':row[2],'Cargo':row[3],'MesAdmissao':row[4],'AnoAdmissao':row[5]})
        f = open('Exportacao/DadosFuncionarios', 'w')
        json.dump(arquivo, f, sort_keys=True, indent=4)
        f.close()

     z = zp.ZipFile('DadosFuncionarios.zip', 'w', zp.ZIP_DEFLATED)
     z.write('Exportacao/DadosFuncionarios')
     z.close()


     print("-----------------------------------------------------------------")
     print("+      Concluido, arquivo de funcionarios gerado com sucesso    +")
     print("-----------------------------------------------------------------")
     Fun.MenuFuncoes(liberacaoAcesso='S')

    except Exception as erro:  
      print(erro)
      print("+           Erro ao exportar dados                             +")
      print("----------------------------------------------------------------")