# Importa a biblioteca que permite fazer requisições HTTP
import requests

def pesquisar_livros(titulo):
    # Define a URL da API do Open Library para pesquisa de livros
    url = "https://openlibrary.org/search.json"

    # O parâmetro params permite enviar informações na URL para a API realizar a pesquisa
    resposta = requests.get(url,params={"title": titulo, "limit": 10}, timeout=15)

    resposta.raise_for_status() # Levanta um erro se a resposta não for bem-sucedida
    dados = resposta.json() # Converte a resposta em JSON para um dicionário Python
    livros = [] # Criamos uma lista vazia para guardar os resultados já organizados

    #Procure a chave "docs" no dicionário dados. Se ela não existir, utilize uma lista vazia []
    for item in dados.get("docs", []):
        livros.append({
            "id_externo": item.get("key"),
            # Se a chave não existir, usa "Sem título" como valor padrão.
            "titulo": item.get("title", "Sem título"),
            # A API pode fornecer vários autores em uma lista
            # O método .join() junta esses nomes em uma única string, separando-os por vírgula e espaço
            "autor": ", ".join(item.get("author_name", ["Autor desconhecido"])),
            "ano": item.get("first_publish_year", "Ano desconhecido")
        })
    # O return devolve a lista para quem chamou a função
    return livros

# Teste temporário da API.
if __name__ == "__main__":
    rel = pesquisar_livros("Harry Potter")

    for livro in rel:
        print(livro)



    
    