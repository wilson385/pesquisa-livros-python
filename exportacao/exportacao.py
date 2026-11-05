# csv: biblioteca que utilizamos para trabalhar com arquivos CSV
import csv
from tkinter import filedialog

def exportar_csv(livros):

    # Verificar se a lista de livros está vazia
    if not livros:
        return None

    #Essa função pertence ao Tkinter e abre uma janela de salvamento de arquivos.
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")], initialfile="livros_exportados.csv", title="Salvar arquivo CSV")

    # Verifica se o usuário cancelou a operação
    if not caminho_arquivo:
        return None

    # Abre o arquivo CSV para escrita
    # "w": abre para escrita. Se já existir um arquivo com esse nome, ele será sobrescrito.
    # newline="": evita que sejam adicionadas linhas em branco extras no arquivo CSV.
    # O as arquivo significa: dar o nome arquivo ao arquivo que o Python abriu
    with open(caminho_arquivo, "w", newline="", encoding="utf-8-sig") as arquivo_csv:

        # Define quais colunas serão exportadas
        colunas = ["id_externo", "titulo", "autor", "ano"]

        # Criar o escritor 
        # DictWriter é uma ferramenta que permite escrever informações de dicionários dentro de um arquivo CSV.
        # fieldnames é o parâmetro que recebe os nomes das colunas.
        # extrasaction="ignore" Significa: ignore as informações extras que não foram definidas nas colunas.
        escritor = csv.DictWriter(arquivo_csv,fieldnames = colunas, extrasaction="ignore", delimiter=";")

        escritor.writeheader() # Escreve o cabeçalho no arquivo CSV

        escritor.writerows(livros) #escreva as linhas correspondentes aos livros dessa lista

        return caminho_arquivo # Retorna o caminho do arquivo CSV exportado
        
        

