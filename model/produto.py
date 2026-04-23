from  database.conexao import conectar

def recuperar():
    # passo 1 e 2 ja feito
        conexao, cursor = conectar()

        cursor.execute("SELECT codigo, produto, descricao, destaque, preco, foto, disponibilidade FROM Produtos;")
  
        #    cursor.execute("SELECT codigo, produto, descricao, preco, foto FROM Produtos")

        #rec os dados
        produtos =  cursor.fetchall()

        # fechar a conexão
        conexao.close()

        return produtos

def rec_destaq():
        conexao, cursor = conectar()

        cursor.execute("SELECT codigo, produto, descricao, destaque, preco, foto, disponibilidade FROM Produtos WHERE destaque = True;")

        produtos =  cursor.fetchall()

       # fechar a conexão
        conexao.close()

        return produtos

def rec_produto(codigo:int):  
        conexao, cursor = conectar()
        cursor.execute("""SELECT codigo, produto, descricao, destaque, preco, foto, disponibilidade FROM Produtos WHERE codigo = %s""", [codigo])

        produto = cursor.fetchone()
        conexao.close()

        return produto