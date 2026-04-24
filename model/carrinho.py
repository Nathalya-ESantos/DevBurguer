from database.conexao import criar_conexao

def recuperar_carrinho(usuario:str) ->list:
    conexao, cursor = criar_conexao()
    cursor.execute("""
                    
                    """)
    
    resultado = cursor.fetchall()
    conexao.close()
    return resultado