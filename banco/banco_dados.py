import psycopg2 as pg

#função para criar as tabelas, verificar dbname=livros e user=postgres e mudar se não forem certos.
def tablemaker():
    conn = psycopg2.connect("dbname=livros user=postgres")
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS livros (id SERIAL PRIMARY KEY, nome VARCHAR(255) NOT NULL, capa BYTEA, ano_de_lan DATE NOT NULL, autor VARCHAR(255) NOT NULL);")
        cur.execute("CREATE TABLE IF NOT EXISTS lojas (id SERIAL PRIMARY KEY, nome  VARCHAR(255) NOT NULL, site TEXT);")
        cur.execute("CREATE TABLE preco (id_livros INT NOT NULL, id_loja INT NOT NULL, preco NUMERIC(10, 2), FOREIGN KEY (id_livros) REFERENCES livros(id), FOREIGN KEY (id_loja) REFERENCES lojas(id));")
        conn.commit()
    except Error:
        print("Falha ao criar mesas") 
    finally: 
        cur.close()
        conn.close()
