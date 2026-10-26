# Importa a biblioteca que permite fazer requisições HTTP
import requests

def pesquisar_livros():
    # Define a URL da API do Open Library para pesquisa de livros
    url = "https://openlibrary.org/search.json"
    titulo = "Homem Aranha"

    # O parâmetro params permite enviar informações na URL para a API realizar a pesquisa
    resposta = requests.get(url,params={"title": titulo, "limit": 10}, timeout=15)
    
    