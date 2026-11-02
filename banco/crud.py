import psycopg2 as pg
from psycopg2 import Error
from banco_dados import conn, encerra_conn

def tablemaker(): 
    conect = conn
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS livros (id_exclusivo VARCHAR(255) PRIMARY KEY, nome VARCHAR(255) NOT NULL, ano_de_lan INTEGER NOT NULL, autor VARCHAR(255) NOT NULL);")
        conn.commit()
    except Error as e:
        print("Falha ao criar mesa") 
    finally: 
        cur.close()
        conect.close()

def bookadd(id_exclusivo, nome, lam, autor): 
    conect = conn
    cur = conn.cursor()
    try:
        q = "INSERT INTO livros (id_exclusivo, nome, ano_de_lan, autor) values (%s, %s, %s, %s);"
        cur.execute(q, [id_exclusivo, nome, lam, autor])
        conn.commit()
    except Error as e:
        print("Falha ao adicionar entrada") 
    finally: 
        cur.close()
        conect.close()
        
def booklook(nome): 
    conect = conn
    cur = conn.cursor()
    try:
        q = "SELECT * FROM livros WHERE nome ILIKE %s;"
        results = cur.fetchall(q, ['%'+nome+'%'])
        return results
    except Error as e:
        print("Falha na pesquisa") 
    finally: 
        cur.close()
        conect.close()
        
def bookdelete(id_exclusivo): 
    conect = conn
    cur = conn.cursor()
    try:
        q = "DELETE FROM livros WHERE = %s;"
        results = cur.execute(q, [id_exclusivo])
        return results
    except Error as e:
        print("Falha ao deletar emtrada") 
    finally: 
        cur.close()
        conect.close()
        
def tableclear(): 
    conect = conn
    cur = conn.cursor()
    try:
        q = "DELETE FROM livros;"
        results = cur.execute(q)
        return results
    except Error as e:
        print("Falha na limpesa") 
    finally: 
        cur.close()
        conect.close()