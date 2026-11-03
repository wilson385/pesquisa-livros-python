# Importar a função responsável pela exportação CSV.
from exportacao.exportacao import exportar_csv

# Importar a função responsável por pesquisar livros na API.
from servicos.coletor import pesquisar_livros

# Importar messagebox para mostrar avisos e erros.
from tkinter import messagebox

# Importar bibliotecas usadas na interface gráfica.
from CTkMessagebox import CTkMessagebox
import customtkinter

# Importar Pillow para trabalhar com imagens.
from PIL import Image, ImageTk


# Configuração geral.
font_name = "Georgia"


# Criar classe do cabeçalho da página.
class HeaderBar(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, height=32, **kwargs)

        # Criar imagem para o ícone de informação.
        info_ico = customtkinter.CTkImage(
            light_image=Image.open("interface/assets/info_ico_d.png"),
            dark_image=Image.open("interface/assets/info_ico_l.png"),
            size=(24, 24)
        )

        # Configurar alinhamento.
        self.grid_columnconfigure(0, weight=1)

        # Criar botão de informação.
        self.button = customtkinter.CTkButton(
            self,
            image=info_ico,
            text="",
            width=32,
            height=32,
            fg_color="transparent",
            corner_radius=0,
            hover_color="#404040",
            command=self.btn_callback
        )
        self.button.grid(row=0, column=0, padx=0, pady=0, sticky="e")

    # Mostrar uma janela com a descrição e os créditos do projeto.
    def btn_callback(self):
        print("Creditado...")

        fnt1 = customtkinter.CTkFont(font_name, 14)

        CTkMessagebox(
            master=self.winfo_toplevel(),
            corner_radius=0,
            font=fnt1,
            title="Descrição.",
            message="Descrição do projeto :\n\nCréditos :",
            icon="interface/assets/info_ico_l.png",
            header=True
        )


# Criar classe da caixa de pesquisa.
class SearchBar(customtkinter.CTkFrame):

    def __init__(self, master, command):
        super().__init__(master, fg_color="transparent")

        # Criar fonte para a caixa de pesquisa.
        fnt1 = customtkinter.CTkFont(font_name, 16)

        # Criar imagem para o ícone de pesquisa.
        search_ico = customtkinter.CTkImage(
            light_image=Image.open("interface/assets/search_ico_d.png"),
            dark_image=Image.open("interface/assets/search_ico_l.png"),
            size=(24, 24)
        )

        # Guardar a função que será executada quando pesquisar.
        self.command = command

        # Configurar alinhamento.
        self.grid_columnconfigure(1, weight=1)

        # Criar botão de pesquisa.
        self.button = customtkinter.CTkButton(
            self,
            image=search_ico,
            font=fnt1,
            text="",
            width=32,
            height=32,
            fg_color="transparent",
            corner_radius=8,
            hover_color="#404040",
            command=self.btn_callback
        )
        self.button.grid(row=0, column=0, padx=0, pady=0, sticky="w")

        # Criar campo de texto.
        self.entry = customtkinter.CTkEntry(
            self,
            font=fnt1,
            placeholder_text="Digite o nome do livro desejado aqui.",
            width=332,
            height=32,
            corner_radius=0,
            fg_color="transparent"
        )
        self.entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="we")

    # Executar a pesquisa quando o usuário clicar no botão.
    def btn_callback(self):
        titulo = self.get_text().strip()

        if titulo != "":
            self.command(titulo)
            self.reset_text()
        else:
            messagebox.showwarning(
                "Atenção",
                "Digite o nome de um livro."
            )

    # Apagar o texto do campo de pesquisa.
    def reset_text(self):
        self.entry.delete(0, "end")

    # Retornar o texto digitado.
    def get_text(self):
        return self.entry.get()


# Criar classe dos livros que serão mostrados na interface.
class Book(customtkinter.CTkFrame):

    def __init__(
        self,
        master,
        image="interface/assets/app_ico.png",
        book_name="Livro X",
        author="X",
        r_date="01/01/0000",
        **kwargs
    ):
        super().__init__(
            master,
            bg_color="transparent",
            border_width=0,
            **kwargs
        )

        fnt1 = customtkinter.CTkFont(font_name, 14)
        fnt2 = customtkinter.CTkFont(font_name, 16)

        # Criar imagem do botão de favoritos.
        bookmark_image = customtkinter.CTkImage(
            light_image=Image.open("interface/assets/bookmark_ico_d.png"),
            dark_image=Image.open("interface/assets/bookmark_ico_l.png"),
            size=(16, 24)
        )

        # Guardar os dados que serão exibidos.
        self.book_image = ImageTk.PhotoImage(file=image)
        self.book_name = book_name
        self.author_text = "Autor(a) : " + author
        self.r_date_text = "Data de lançamento : " + r_date

        # Configurar alinhamento.
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=0)

        # Exibir imagem do livro.
        self.image = customtkinter.CTkLabel(
            self,
            corner_radius=0,
            bg_color="transparent",
            font=fnt2,
            text="",
            image=self.book_image,
            anchor="nw"
        )
        self.image.grid(row=0, column=0, padx=(20, 0), pady=0, sticky="nw")

        # Criar quadro com as informações do livro.
        self.frame1 = customtkinter.CTkFrame(
            self,
            width=128,
            height=128,
            corner_radius=0,
            fg_color="transparent"
        )
        self.frame1.grid(row=0, column=1, sticky="nw")

        # Exibir título.
        self.name = customtkinter.CTkLabel(
            self.frame1,
            corner_radius=0,
            bg_color="transparent",
            font=fnt2,
            text=self.book_name,
            anchor="nw"
        )
        self.name.grid(row=0, column=0, padx=0, pady=0, sticky="nw")

        # Exibir autor.
        self.author = customtkinter.CTkLabel(
            self.frame1,
            corner_radius=0,
            bg_color="transparent",
            font=fnt1,
            text_color="#bfbfbf",
            text=self.author_text,
            anchor="nw"
        )
        self.author.grid(row=1, column=0, padx=0, pady=0, sticky="nw")

        # Exibir data de lançamento.
        self.r_date = customtkinter.CTkLabel(
            self.frame1,
            corner_radius=0,
            bg_color="transparent",
            font=fnt1,
            text_color="#bfbfbf",
            text=self.r_date_text,
            anchor="nw"
        )
        self.r_date.grid(row=2, column=0, padx=0, pady=0, sticky="nw")

        # Criar quadro do botão de favoritos.
        self.frame2 = customtkinter.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent"
        )
        self.frame2.grid(row=0, column=2, sticky="ne")

        # Criar botão de favoritos.
        self.bookmark = customtkinter.CTkButton(
            self.frame2,
            width=32,
            height=32,
            corner_radius=8,
            hover_color="#404040",
            fg_color="transparent",
            bg_color="transparent",
            font=fnt1,
            text="",
            image=bookmark_image,
            command=self.btn_callback
        )
        self.bookmark.grid(row=0, column=0, padx=0, pady=0, sticky="ne")

    def btn_callback(self):
        self.add_bookmark()

        # Fazer mais coisas aqui futuramente.

    # Retornar os dados básicos do livro.
    def get_data(self):
        return {
            "titulo": self.book_name,
            "autor": self.author_text,
            "ano": self.r_date_text
        }

    # Adicionar o livro aos favoritos.
    def add_bookmark(self):
        print("Bookmarked : " + self.book_name)

        # Fazer mais coisas aqui futuramente.


# Criar classe do painel que mostra os resultados da pesquisa.
class Results(customtkinter.CTkScrollableFrame):

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            label_text="Resultados :",
            corner_radius=0,
            height=400,
            **kwargs
        )

        # ScrollableFrame Widget tem um problema de lag.
        # Por enquanto, manteremos esse componente.

        # Configuração.
        self.grid_columnconfigure(0, weight=1)

        # Listas que guardam os dados e os componentes visuais.
        self.book_data_list = []
        self.book_widget_list = []

    # Limpar os resultados anteriores.
    def refresh(self):
        for widget in self.book_widget_list:
            widget.destroy()

        self.book_widget_list = []
        self.book_data_list = []

    # Pesquisar livros na API e mostrar os resultados.
    def buscar(self, titulo):
        self.refresh()

        try:
            livros = pesquisar_livros(titulo)

            # Guardar os dados recebidos da API.
            self.book_data_list = livros

            # Avisar se nenhum livro for encontrado.
            if not livros:
                mensagem = customtkinter.CTkLabel(
                    self,
                    text="Nenhum livro encontrado."
                )

                mensagem.grid(
                    row=0,
                    column=0,
                    padx=5,
                    pady=15,
                    sticky="we"
                )

                self.book_widget_list.append(mensagem)
                return

            # Criar um componente visual para cada livro.
            for i, livro in enumerate(livros):
                ano = livro.get("ano")

                book = Book(
                    self,
                    book_name=livro.get("titulo") or "Sem título",
                    author=livro.get("autor") or "Autor desconhecido",
                    r_date=str(ano) if ano else "Não informado"
                )

                book.grid(
                    row=i,
                    column=0,
                    padx=5,
                    pady=(15, 5),
                    sticky="we"
                )

                self.book_widget_list.append(book)

        except Exception as erro:
            messagebox.showerror(
                "Erro na pesquisa",
                f"Não foi possível buscar os livros.\n{erro}"
            )

    # NOVO: exportar os livros encontrados para CSV.
    def exportar(self):

        # Verificar se existem livros para exportar.
        if not self.book_data_list:
            messagebox.showwarning(
                "Atenção",
                "Não existem livros para exportar."
            )
            return

        # Chamar a função do arquivo exportacao.py.
        caminho = exportar_csv(self.book_data_list)

        # Se o usuário não cancelou e o arquivo foi salvo, avisar.
        if caminho:
            messagebox.showinfo(
                "Exportação concluída",
                f"Arquivo salvo com sucesso!\n{caminho}"
            )


# Criar classe principal do aplicativo.
class App(customtkinter.CTk):

    def __init__(
        self,
        title="Nome do Programa",
        geometry="540x700",
        fg_color=None,
        **kwargs
    ):
        super().__init__(fg_color, **kwargs)

        app_ico = ImageTk.PhotoImage(file="interface/assets/app_ico.png")

        # Configurações da janela.
        self.title(title)
        self.wm_iconbitmap()
        self.iconphoto(False, app_ico)
        self.geometry(geometry)
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

        # Instanciar cabeçalho.
        self.header = HeaderBar(self)
        self.header.grid(
            row=0,
            column=0,
            padx=0,
            pady=(0, 0),
            sticky="ew"
        )

        # Instanciar painel de resultados.
        self.results = Results(self)
        self.results.grid(
            row=2,
            column=0,
            padx=40,
            pady=(20, 15),
            sticky="nsew"
        )

        # Instanciar caixa de pesquisa e conectá-la à pesquisa dos resultados.
        self.searchBar = SearchBar(self, self.results.buscar)
        self.searchBar.grid(
            row=1,
            column=0,
            padx=80,
            pady=(40, 20),
            sticky="ew"
        )

        # NOVO: botão para exportar os resultados da pesquisa.
        self.export_button = customtkinter.CTkButton(
            self,
            text="Exportar CSV",
            command=self.results.exportar
        )
        self.export_button.grid(
            row=3,
            column=0,
            padx=80,
            pady=(0, 20),
            sticky="ew"
        )

# Ponto de entrada do aplicativo.
# Execute main.py para iniciar a aplicação.
