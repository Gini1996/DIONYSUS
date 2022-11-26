import psycopg2 as bd

def InserirCompra():
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
     print("+  Digite o fornecedor :                        +")
     print("-------------------------------------------------")
     fornecedor = input("")
     print("-------------------------------------------------")
     print("+  Digite a quantidade do produto:              +")
     print("-------------------------------------------------")
     qtd = int(input(""))
     print("-------------------------------------------------")
     sql = f"INSERT INTO compra (produto,fornecedor,quantidade) values ('{nome}','{fornecedor}','{qtd}') RETURNING produto,fornecedor,quantidade;"
     cur = con.cursor()
     cur.execute(sql)
     con.commit()
     con.close() 

     print("+        Compra Inserida com sucesso!           +")
     print("-------------------------------------------------")
     print("\n")
    except Exception as erro:  
        print("+           Erro ao inserir compra              +")
        print("-------------------------------------------------")

def VisualizaCompra():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     cursor = con.cursor()
     Qy = "select * from compra"

     cursor.execute(Qy)
     func = cursor.fetchall()
     print("-------------------------------------------------")
     print("+     Lista de compra cadastrada                +")
     print("-------------------------------------------------")
     for row in func:
        print("Id = ", row[0], )
        print("Produto = ", row[1])
        print("Fornecedor = ", row[2])
        print("Quantidade = ", row[3], "\n")
        print("-------------------------------------------------")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao localizar compra            +")
      print("-------------------------------------------------")

def DeletaCompra():
    try:
     con = bd.connect(
         database="Dionysus",
         user="postgres",
         password="admin",
         host="localhost",
         port="5432"
     )
     print("-------------------------------------------------")
     print("+ Digite o Id da compra que sera excluido:      +")
     print("-------------------------------------------------")
     id = int(input(""))
     sql = f"DELETE FROM compra WHERE idcompra = '{id}';"
     cur = con.cursor()
     cur.execute(sql)
     con.commit()
     con.close() 
     
     print("-------------------------------------------------")
     print("+        Compra Excluida com sucesso!           +")
     print("-------------------------------------------------")
     print("\n")

    except Exception as erro:  
      print(erro)
      print("+           Erro ao excluir a compra            +")
      print("-------------------------------------------------")