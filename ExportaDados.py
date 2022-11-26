import psycopg2 as bd
import json 
import Funcionalidades as Fun

def GerarJSON():
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
     QyEstoque = "select * from estoque"
     QyFuncionarios = "select * from funcionarios"
     QyLogin = "select * from login_sistema"

     cursor.execute(QyCompra)
    #  cursor.execute(QyEstoque)
    #  cursor.execute(QyFuncionarios)
    #  cursor.execute(QyLogin)
     
     arquivo = []

     funcCompra = cursor.fetchall()
     for row in funcCompra:
        arquivo.append({'Tabela':'Compra','Id':row[0],'Produto':row[1],'Fornecedor':row[2],'Quantidade':row[3]})
        f = open('DadosExportados', 'w')
        json.dump(arquivo, f, sort_keys=True, indent=4)
        f.close()

    #  funcEstoque = cursor.fetchall()
    #  for row in funcEstoque:
    #     arquivo.append({'Tabela':'Estoque','Id':row[0],'Produto':row[1],'Perecivel':row[2],'Quantidade':row[3],'PrecoCusto':row[4],'PrecoVenda':row[5]})
    #     f = json.load(arquivo)
    #     json.dump(arquivo, f, sort_keys=True, indent=4)
    #     f.close()

    #  funcFuncionarios = cursor.fetchall()
    #  for row in funcFuncionarios:
    #     arquivo.append({'Tabela':'Funcionarios','Id':row[0],'Nome':row[1],'Sobrenome':row[2],'Cargo':row[3],'MesAdmissao':row[4],'AnoAdmissao':row[5]})
    #     f = json.load(arquivo)
    #     json.dump(arquivo, f, sort_keys=True, indent=4)
    #     f.close()

    #  funcLogin = cursor.fetchall()
    #  for row in funcLogin:
    #     arquivo.append({'Tabela':'Login_sistema','Id':row[0],'Usuario':row[1],'Senha':row[2],'Nome':row[3],'Sobrenome':row[4]})
    #     f = json.load(arquivo)
    #     json.dump(arquivo, f, sort_keys=True, indent=4)
    #     f.close()


     print("-------------------------------------------------")
     print("+      Concluido, arquivo gerado com sucesso    +")
     print("-------------------------------------------------")
     Fun.MenuFuncoes(liberacaoAcesso='S')

    except Exception as erro:  
      print(erro)
      print("+           Erro ao exportar dados              +")
      print("-------------------------------------------------")