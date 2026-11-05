import psycopg2 as pg
from psycopg2 import Error
from banco_dados import conexao, encerra_conn

#cria a tabela
def tablemaker():
    conect = conexao()
    cur = conect.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS livros (id_exclusivo VARCHAR(255) PRIMARY KEY, nome VARCHAR(255) NOT NULL, ano_de_lan INTEGER NOT NULL, autor VARCHAR(255) NOT NULL);")
        conect.commit()
    except Error as e:
        print("Falha ao criar mesa") 
    finally: 
        cur.close()
        conect.close()

#adiciona entradas na tabela na ordem: ID, nome, ano de lançamento, autor
def bookadd(id_exclusivo, nome, lam, autor):
    conect = conexao()
    cur = conect.cursor()
    try:
        q = "INSERT INTO livros (id_exclusivo, nome, ano_de_lan, autor) values (%s, %s, %s, %s);"
        cur.execute(q, [id_exclusivo, nome, lam, autor])
        conect.commit()
    except Error as e:
        print("Falha ao adicionar entrada") 
    finally: 
        cur.close()
        conect.close()

#procura for uma entrada specifica baseado no nome        
def booklook(nome):
    conect = conexao()
    cur = conect.cursor()
    try:
        q = "SELECT * FROM livros WHERE nome ILIKE %s;"
        results = cur.fetchall(q, ['%'+nome+'%'])
        return results
    except Error as e:
        print("Falha na pesquisa") 
    finally: 
        cur.close()
        conect.close()

#mostra a tabela inteira       
def tablelook():
    conect = conexao()
    cur = conect.cursor()
    try:
        q = "SELECT * FROM livros;"
        results = cur.fetchall(q)
        return results
    except Error as e:
        print("Falha na aquisição") 
    finally: 
        cur.close()
        conect.close()

#deleta uma entrada specifica de acordo on o id dela        
def bookdelete(id_exclusivo):
    conect = conexao()
    cur = conect.cursor()
    try:
        q = "DELETE FROM livros WHERE = %s;"
        results = cur.execute(q, [id_exclusivo])
        conect.commit()
    except Error as e:
        print("Falha ao deletar emtrada") 
    finally: 
        cur.close()
        conect.close()

#deleta todas as entradas     
def tableclear():
    conect = conexao()
    cur = conect.cursor()
    try:
        q = "DELETE FROM livros;"
        results = cur.execute(q)
        conect.commit()
    except Error as e:
        print("Falha na limpesa") 
    finally: 
        cur.close()
        conect.close()
