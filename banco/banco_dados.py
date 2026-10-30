import psycopg2 as pg
from psycopg2 import Error
import os
from dotenv import load_dotenv

load_dotenv()

def conn():
    try:
        pwd = os.getenv("DB_PASSWORD")
        conexao = pg.connect(
            user = "postgres",
            password = pwd,
            host = "localhost",
            port = "5432",
            database = "Pesquisa_livros" )

        print("Conexao realizada com sucesso!!")

        return conn

    except Error as e:
        print(f"Erro ao tentar conectar com o banco de dados {e}")

def encerra_conn(conn):
    if conn:
        conn.close()
        print("Conexao encerrada!!")

#Conexao ao banco de dados Postgresql
