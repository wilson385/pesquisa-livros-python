
# Importar a classe principal da interface.
from interface.tela_principal import App

# Importar a função que cria a tabela do banco de dados.
from banco.crud import tablemaker

# Função principal do programa.
def main():
    # Criar a tabela do banco de dados, caso ainda não exista.
    tablemaker()

    # Criar e iniciar a janela principal do aplicativo.
    app = App("Pesquisa de Livros", "540x648")
    app.mainloop()

# Se este arquivo estiver sendo executado diretamente, execute o código que está abaixo.
# Executar o programa.
if __name__ == "__main__":
    main()
