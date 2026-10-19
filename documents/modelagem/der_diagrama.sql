CREATE TABLE tb_usuario (
 login VARCHAR(15) NOT NULL,
 senha VARCHAR(200)
);

ALTER TABLE tb_usuario ADD CONSTRAINT PK_tb_usuario PRIMARY KEY (login);


CREATE TABLE tb_categoria (
 id_categoria INT NOT NULL,
 nome VARCHAR(25),
 login VARCHAR(15)
);

ALTER TABLE tb_categoria ADD CONSTRAINT PK_tb_categoria PRIMARY KEY (id_categoria);


CREATE TABLE tb_despesa (
 id_despesa INT NOT NULL,
 data DATE,
 hora TIME(4),
 valor FLOAT(4),
 decricao VARCHAR(50),
 tipo VARCHAR(15),
 login VARCHAR(15) NOT NULL,
 id_categoria INT
);

ALTER TABLE tb_despesa ADD CONSTRAINT PK_tb_despesa PRIMARY KEY (id_despesa);


ALTER TABLE tb_categoria ADD CONSTRAINT FK_tb_categoria_0 FOREIGN KEY (login) REFERENCES tb_usuario (login);


ALTER TABLE tb_despesa ADD CONSTRAINT FK_tb_despesa_0 FOREIGN KEY (login) REFERENCES tb_usuario (login);
ALTER TABLE tb_despesa ADD CONSTRAINT FK_tb_despesa_1 FOREIGN KEY (id_categoria) REFERENCES tb_categoria (id_categoria);


