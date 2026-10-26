CREATE TABLE Livros (
id SERIAL PRIMARY KEY, 
nome  VARCHAR(255) NOT NULL,
capa BYTEA,
ano_de_lan DATE NOT NULL,
autor VARCHAR(255) NOT NULL
);
CREATE TABLE lojas (
id SERIAL PRIMARY KEY, 
nome  VARCHAR(255) NOT NULL,
site TEXT
);
CREATE TABLE preco (
id_livros INT NOT NULL,
id_loja INT NOT NULL,
preco NUMERIC(10, 2),
FOREIGN KEY (id_livros) REFERENCES Livros(id),
FOREIGN KEY (id_loja) REFERENCES lojas(id)
);

#linhas de commando para a base de dados.
