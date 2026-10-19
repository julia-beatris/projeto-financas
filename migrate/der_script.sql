create database if not exists projeto_financa;
use projeto_financa;

CREATE TABLE if not exists tb_usuario (
 login VARCHAR(15) NOT NULL PRIMARY KEY,
 senha VARCHAR(200)
);


CREATE TABLE if not exists tb_categoria (
 id_categoria INT NOT NULL PRIMARY KEY auto_increment,
 nome VARCHAR(25),
 login VARCHAR(15)
);



CREATE TABLE if not exists tb_despesa (
 id_despesa INT NOT NULL PRIMARY KEY auto_increment,
 data DATE,
 hora TIME(4),
 valor FLOAT(4),
 decricao VARCHAR(50),
 tipo VARCHAR(15),
 login VARCHAR(15) NOT NULL,
 id_categoria INT
);


ALTER TABLE tb_categoria ADD CONSTRAINT FK_tb_categoria_0 FOREIGN KEY (login) REFERENCES tb_usuario (login);

ALTER TABLE tb_despesa ADD CONSTRAINT FK_tb_despesa_0 FOREIGN KEY (login) REFERENCES tb_usuario (login);
ALTER TABLE tb_despesa ADD CONSTRAINT FK_tb_despesa_1 FOREIGN KEY (id_categoria) REFERENCES tb_categoria (id_categoria);





