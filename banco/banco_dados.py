import psycopg2 as pg

#função para criar a tabela, verificar dbname=livros e user=postgres e mudar se não forem certos.
def tablemaker():
    conn = psycopg2.connect("dbname=livros user=postgres")
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS livros (id VARCHAR(255) PRIMARY KEY, nome VARCHAR(255) NOT NULL, capa BYTEA, ano_de_lan DATE NOT NULL, autor VARCHAR(255) NOT NULL);")
        conn.commit()
    except Error:
        print("Falha ao criar mesa") 
    finally: 
        cur.close()
        conn.close()
#função para adicionar uma entrada, verificar dbname=livros e user=postgres e mudar se não forem certos.
def bookadd(id, nome, capa, lam, autor):
    conn = psycopg2.connect("dbname=livros user=postgres")
    cur = conn.cursor()
    try:
        q = "insert into livros (id, nome, capa, ano_de_lan, autor) values (%s, %s, %s, %s, %s);"
        cur.execute(q, [id, nome, capa, lam, autor])
        conn.commit()
    except Error:
        print("Falha ao adicionar entrada") 
    finally: 
        cur.close()
        conn.close()
