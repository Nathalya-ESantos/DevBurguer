CREATE DATABASE IF NOT EXISTS Produtos;
USE Produtos;

CREATE TABLE IF NOT EXISTS Produtos (
    CODIGO INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    PRODUTO VARCHAR(50),
    DESCRICAO VARCHAR(200),
    DESTAQUE BOOL,
    PRECO FLOAT,
    FOTO VARCHAR(270),
    DISPONIBILIDADE BOOL
);

CREATE TABLE IF NOT EXISTS Usuarios (
    USUARIO VARCHAR(20) PRIMARY KEY,
    SENHA VARCHAR(200) NOT NULL,
    NOME VARCHAR(100) DEFAULT 'ANONIMO'
);

CREATE TABLE IF NOT EXISTS Carrinhos (
    COD_CARRINHO INT AUTO_INCREMENT PRIMARY KEY,
    USUARIO VARCHAR(20),
    DATA DATETIME DEFAULT CURRENT_TIMESTAMP,
    FINALIZADO BOOL,
    
    CONSTRAINT FK_CARRINHO_USUARIO 
    FOREIGN KEY (USUARIO) 
    REFERENCES Usuarios(USUARIO)
);

CREATE TABLE IF NOT EXISTS Itens_Carrinhos (
    COD_ITENS_CARRINHOS INT AUTO_INCREMENT PRIMARY KEY,
    COD_CARRINHO INT,
    COD_PRODUTO INT,
    QUANTIDADE INT DEFAULT 1,

    CONSTRAINT FK_ITENSCARRINHO_CARRINHOS 
    FOREIGN KEY (COD_CARRINHO) 
    REFERENCES Carrinhos(COD_CARRINHO),

    CONSTRAINT FK_ITENSCARRINHO_PRODUTO 
    FOREIGN KEY (COD_PRODUTO) 
    REFERENCES Produtos(CODIGO)
);

INSERT IGNORE INTO Usuarios (USUARIO, SENHA, NOME) VALUES ('nathalya', '123', 'nathy');
INSERT IGNORE INTO Usuarios (USUARIO, SENHA, NOME) VALUES ('godofredo', '1234', 'godosantos');
INSERT IGNORE INTO Usuarios (USUARIO, SENHA, NOME) VALUES ('godothalya', '6969', 'godofredo');

INSERT INTO Produtos (PRODUTO, DESCRICAO, DESTAQUE, PRECO, FOTO, DISPONIBILIDADE) VALUES
('hamburguer 2', 'gostoso', 1, 37.90, 'https://cloudfront-us-east-1.images.arcpublishing.com/estadao/77XTHHCCLBEXLC2Y5RK4PN37CE.jpg', 1),
('hamburguer 3', 'muito bom', 1, 56.90, 'https://www.seara.com.br/wp-content/uploads/2025/09/shutterstock_1489640750-1.jpg', 1),
('X-Burguer', 'Hamburguer com queijo e molho especial', 1, 18.90, 'https://www.sabornamesa.com.br/media/k2/items/cache/bf26253d7b8f171dddb155f84ce1d562_XL.jpg', 1),
('X-Salada', 'Hamburguer com queijo, alface e tomate', 1, 21.50, 'https://www.comidaereceitas.com.br/wp-content/uploads/2025/08/foto-cheese-salada-780x519.jpg', 1),
('X-Bacon', 'Hamburguer com bacon crocante e cheddar', 1, 25.00, 'https://www.sabornamesa.com.br/media/k2/items/cache/5098e75e57e36807c173cb7490b1b0d2_XL.jpg', 1),
('X-Tudo', 'Hamburguer completo com bacon, ovo e salada', 1, 32.90, 'https://alemaolanches.festzap.com.br/_core/_uploads//2022/05/111914052238abagj4gk.jpg', 1),
('Batata Frita', 'Porção de batata frita crocante', 1, 14.00, 'https://jornalsemanario.com.br/wp-content/uploads/batatafrita1.jpg', 1),
('Coca-Cola 2L', 'Refrigerante Coca-Cola 2 litros', 1, 12.00, 'https://img.cdndsgni.com/preview/11077304-m.jpg', 1),
('MilkShake Chocolate', 'Milkshake sabor chocolate', 1, 16.50, 'https://northernvirginiamag.com/wp-content/uploads/2022/08/milkshake.jpg', 1),
('Hot Dog Especial', 'Cachorro quente com pure e batata palha', 1, 17.90, 'https://s2.glbimg.com/XQq5qXrTCA2t19Nnlo-sIa-ilH4=/620x455/e.glbimg.com/og/ed/f/original/2019/09/13/cachorro-quente-brasileiro.jpg', 1);

INSERT INTO Carrinhos (USUARIO, FINALIZADO) VALUES ('godothalya', 0);

INSERT INTO Itens_Carrinhos (COD_CARRINHO, COD_PRODUTO, QUANTIDADE) VALUES (1, 1, 2);

SELECT 
    Carrinhos.COD_CARRINHO,
    Usuarios.USUARIO,
    Carrinhos.DATA,
    Carrinhos.FINALIZADO,
    Produtos.PRODUTO,
    Itens_Carrinhos.QUANTIDADE,
    Produtos.PRECO,
    Produtos.FOTO
FROM Carrinhos
INNER JOIN Usuarios ON Usuarios.USUARIO = Carrinhos.USUARIO
INNER JOIN Itens_Carrinhos ON Carrinhos.COD_CARRINHO = Itens_Carrinhos.COD_CARRINHO
INNER JOIN Produtos ON Produtos.CODIGO = Itens_Carrinhos.COD_PRODUTO
WHERE Usuarios.USUARIO = 'godothalya';