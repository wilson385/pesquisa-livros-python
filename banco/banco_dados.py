import psycopg2 as pg #Biblioteca do PostgreSQL
from psycopg2 import Error
import os #Comandos do SO
from dotenv import load_dotenv 

load_dotenv() #Ler o arquivo .env

pwd = os.getenv("DB_PASSWORD") #Busca a senha do banco

#Funçao para fazer conexao
def conexao():
    try:
        conn = pg.connect(
            user = "postgres",
            password = pwd,
            host = "localhost",
            port = "5432",
            dbname = "livros" )
        
        print("Conexao realizada com sucesso!!")
        return conn

    except Error as e:
        print(f"Erro ao tentar conectar com o banco de dados {e}")

#Funçao para encerrar conexao
def encerra_conn(conn):
    if conn:
        conn.close()
        print("Conexao encerrada!!")

#Conexao ao banco de dados Postgresql
