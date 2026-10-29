import psycopg2 as pg

#função para criar as tabelas, verificar dbname=livros e user=postgres e mudar se não forem certos.
def tablemaker():
    conn = pg.connect("dbname=livros user=postgres")
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS livros (id SERIAL PRIMARY KEY, nome VARCHAR(255) NOT NULL, capa BYTEA, ano_de_lan DATE NOT NULL, autor VARCHAR(255) NOT NULL);")
        conn.commit()
    except Error:
        print("Falha ao criar mesas") 
    finally: 
        cur.close()
        conn.close()
