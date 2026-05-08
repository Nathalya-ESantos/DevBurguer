from database.conexao import conectar

class Usuario:
    def __init__(self, usuario:str, senha:str, nome:str=None):
        self.usuario = usuario
        self.senha = senha 
        self.nome = nome

    def cadastrar(self):
        conexao, cursor = conectar() 
        cursor.execute("""
        INSERT INTO Usuarios (usuario, senha, nome)
        VALUES (%s, %s, %s);""", 
        [self.usuario, self.senha, self.nome])

        conexao.commit()
        conexao.close()

    @staticmethod
    def logar(usuario: str, senha: str) -> dict:
        conexao, cursor = conectar()
        cursor.execute("""
            SELECT * FROM Usuarios WHERE usuario = %s AND senha = %s;
        """, (usuario, senha))
        
        resultado = cursor.fetchone()
        conexao.close()
        return resultado