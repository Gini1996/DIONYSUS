import Funcionalidades as Fun
import urllib.request 
import psycopg2 as bd

def ImportaInfo():
    try:
      con = bd.connect(
       database="Dionysus",
       user="postgres",
       password="admin",
       host="localhost",
       port="5432"
      )

      URL = "https://www.google.com/"
      response = urllib.request.urlopen(URL)
      
      headers = response.info()

      dataReq = ("%s" %headers['date'])
      serverReq = ("%s" %headers['server'])
      
      dados = response.read()
      tamanhoReq = ("%d" %len(dados))

      sql = f"INSERT INTO req (url,dtreq,server,tamanhoreq) values ('{URL}','{dataReq}','{serverReq}','{tamanhoReq}') RETURNING url,dtreq,server,tamanhoreq;"
      cur = con.cursor()
      cur.execute(sql)
      con.commit()
      con.close() 

      print("-------------------------------------------------")
      print("+           Dados Importados com sucesso        +")
      print("-------------------------------------------------")

    except Exception as erro:  
        print("+           Erro ao importar dados              +")
        print("-------------------------------------------------")


def VisualizaDados():
   try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     cursor = con.cursor()
     Qy = "select * from req"

     cursor.execute(Qy)
     func = cursor.fetchall()
     print("-------------------------------------------------")
     print("+     Lista de requisicoes                      +")
     print("-------------------------------------------------")
     for row in func:
        print("Id = ", row[0], )
        print("URL = ", row[1])
        print("Data Requisicao = ", row[2])
        print("Servidor = ", row[3],)
        print("Tamanho Requisicao = ", row[4], "\n")
        print("-------------------------------------------------")

     print("---------------------------------------------------------------------------------------------------")
     print("+   Pressione 9 para voltar ao inicio                                                             +")
     print("---------------------------------------------------------------------------------------------------")
  
     btVolta = int(input(""))
  
     if btVolta == 9:
         Fun.MenuFuncoes(liberacaoAcesso='S')

   except Exception as erro:  
      print(erro)
      print("+           Erro ao localizar requisicao        +")
      print("-------------------------------------------------")
