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
      print("DATA* : ")
      print(dataReq)

      serverReq = ("%s" %headers['server'])
      print("SERVER* : ")
      print(serverReq)
      
      dados = response.read()
      tamanhoReq = ("%d" %len(dados))
      print("LENGHT* ")
      print(tamanhoReq)

    except Exception as erro:  
        print("+           Erro ao importar dados              +")
        print("-------------------------------------------------")

    #Fun.MenuFuncoes(liberacaoAcesso='S')