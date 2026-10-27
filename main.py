
# Importar a classe principal da interface.
from interface.tela_principal import App

# Importar a função que cria a tabela do banco de dados.
# from banco.banco_dados import criar_tabela


# Função principal do programa.
def main():
    # Criar a tabela do banco de dados, caso ainda não exista.
    # criar_tabela()

    # Criar e iniciar a janela principal do aplicativo.
    app = App("Pesquisa de Livros", "540x648")
    app.mainloop()


# Executar o programa.
if __name__ == "__main__":
    main()
