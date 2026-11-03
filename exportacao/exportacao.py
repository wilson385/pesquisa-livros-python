
import csv
from tkinter import filedialog

def exportar_csv(livros):

    # Verificar se a lista de livros está vazia
    if not livros:
        return None

    #Essa função pertence ao Tkinter e abre uma janela de salvamento de arquivos.
    arquivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")], initialfile="livros_exportados.csv", title="Salvar arquivo CSV")

    # Verifica se o usuário cancelou a operação
    if not arquivo:
        return None

    # Abre o arquivo CSV para escrita
    with open(arquivo, "w", newline="", encoding="utf-8-sig") as arquivo:

        # Define quais colunas serão exportadas
        colunas = ["id_externo", "titulo", "autor", "ano"]

        # Criar o escritor 
        # DictWriter é uma ferramenta que permite escrever informações de dicionários dentro de um arquivo CSV.
        # fieldnames é o parâmetro que recebe os nomes das colunas.
        # extrasaction="ignore" Significa: ignore as informações extras que não foram definidas nas colunas.
        escritor = csv.DictWriter(arquivo,fieldnames = colunas, extrasaction="ignore", delimiter=";")

        escritor.writeheader() # Escreve o cabeçalho no arquivo CSV

        escritor.writerows(livros) #escreva as linhas correspondentes aos livros dessa lista

        return arquivo # Retorna o caminho do arquivo CSV exportado
        
        

