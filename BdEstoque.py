import psycopg2 as bd

def InserirEstoque():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     
     print("-------------------------------------------------")
     print("+  Digite o nome do produto:                    +")
     print("-------------------------------------------------")
     nome = input("")
     print("-------------------------------------------------")
     print("+  O produto e perecivel? S/N :                 +")
     print("-------------------------------------------------")
     perecivel = input("")
     print("-------------------------------------------------")
     print("+  Digite a quantidade do produto:              +")
     print("-------------------------------------------------")
     qtd = input("")
     print("-------------------------------------------------")
     print("+  Digite o preco de custo:                     +")
     print("-------------------------------------------------")
     custo = int(input(""))
     print("-------------------------------------------------")
     print("+  Digite o preco de venda:                     +")
     print("-------------------------------------------------")
     venda = int(input(""))
     print("-------------------------------------------------")
     sql = f"INSERT INTO estoque (produto,perecivel,quantidade,precobase,precovenda) values ('{nome}','{perecivel}','{qtd}','{custo}','{venda}') RETURNING produto,perecivel,quantidade,precobase,precovenda;"
     cur = con.cursor()
     cur.execute(sql)
     con.commit()
     con.close() 

     print("+        Produto Inserido com sucesso!          +")
     print("-------------------------------------------------")
     print("\n")
    except Exception as erro:  
        print("+           Erro ao inserir produto             +")
        print("-------------------------------------------------")

def VisualizaEstoque():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     cursor = con.cursor()
     Qy = "select * from estoque"

     cursor.execute(Qy)
     func = cursor.fetchall()
     print("-------------------------------------------------")
     print("+     Lista de produtos cadastrados             +")
     print("-------------------------------------------------")
     for row in func:
        print("Id = ", row[0], )
        print("Produto = ", row[1])
        print("Perecivel = ", row[2])
        print("Quantidade = ", row[3])
        print("Preco de custo = ", row[4])
        print("Preco de venda = ", row[5], "\n")
        print("-------------------------------------------------")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao localizar produtos          +")
      print("-------------------------------------------------")

def DeletaEstoque():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     print("-------------------------------------------------")
     print("+ Digite o Id do produto que sera excluido:     +")
     print("-------------------------------------------------")
     id = int(input(""))
     sql = f"DELETE FROM estoque WHERE idprod = '{id}';"
     cur = con.cursor()
     cur.execute(sql)
     con.commit()
     con.close() 
     
     print("-------------------------------------------------")
     print("+        Produto Excluido com sucesso!          +")
     print("-------------------------------------------------")
     print("\n")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao excluir o produto           +")
      print("-------------------------------------------------")