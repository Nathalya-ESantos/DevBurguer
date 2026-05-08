from database.conexao import conectar


def recuperar_carrinho(usuario: str) -> list:
    conexao, cursor = conectar()

    cursor.execute("""
        SELECT 
            p.PRODUTO,
            ic.QUANTIDADE,
            p.PRECO
        FROM Itens_Carrinhos ic
        JOIN Produtos p 
            ON p.CODIGO = ic.COD_PRODUTO
        JOIN Carrinhos c 
            ON c.COD_CARRINHO = ic.COD_CARRINHO
        WHERE c.USUARIO = %s
    """, [usuario])

    resultado = cursor.fetchall()

    conexao.close()

    return resultado


def inserir_item(usuario, cod_produto, quantidade):
    conexao, cursor = conectar()

    
    cursor.execute("""
        SELECT COD_CARRINHO
        FROM Carrinhos
        WHERE USUARIO = %s
        AND FINALIZADO = 0
        LIMIT 1;
    """, [usuario])

    resultado_carrinho = cursor.fetchone()

    
    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho["COD_CARRINHO"]

   
    else:
        cursor.execute("""
            INSERT INTO Carrinhos (USUARIO)
            VALUES (%s);
        """, [usuario])

        codigo_carrinho = cursor.lastrowid

    
    cursor.execute("""
        INSERT INTO Itens_Carrinhos
        (COD_CARRINHO, COD_PRODUTO, QUANTIDADE)
        VALUES (%s, %s, %s);
    """, [codigo_carrinho, cod_produto, quantidade])

    conexao.commit()
    conexao.close()