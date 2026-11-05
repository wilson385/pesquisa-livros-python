#Biblioteca que permite Python fazer requisiçoes HTTP
import requests

#Guardando o endereço da API em uma variavel fixa
url = "https://openlibrary.org/search.json"

#Funçao para buscar os livros
def buscar_livros(termo, limite = 20, ordem = None):
    params = {
        "q": termo, #Texto da busca de acordo com o que o cliente digitou
        "fields": "key, title, first_publish_year, author_name", #Campos que vao ser recbidos pela API
        "limit": limite, #Limite de resultados
    }
    
    resposta = requests.get(url, params=params, timeout=30) #Envia as informaçoes na url para a API pesquisar os dados, timeout -> sem respostas, para de espera(para nao deixar o programa travado)
    resposta.raise_for_status() #Levanta um erro caso a resposta nao foi bem-sucedida
    return resposta.json()["docs"] #Entrega a lista de livros convertendo o texto JSON em dicionario Python, docs->pega somente a lista