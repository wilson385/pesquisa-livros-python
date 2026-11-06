# Importar a função responsável pela exportação CSV.
from exportacao.exportacao import exportar_csv

# Importar a função responsável por pesquisar livros na API.
from servicos.coletor import pesquisar_livros

# Importar messagebox para mostrar avisos e erros.
from tkinter import messagebox

# Importar bibliotecas usadas na interface gráfica.
import customtkinter

# Importar Pillow para trabalhar com imagens.
from PIL import Image, ImageTk

# Importar tablelook, bookdelete e tableclear para mostrar e manusear entradas
#from banco.crud import tablelook, bookdelete, tableclear

# Configuração geral.
font_name = "Georgia"

# Criar classe da janela de informação do banco de dados.
class CreditsInfoWindow(customtkinter.CTkToplevel):
    def __init__(self, master, title="Créditos", *args, **kwargs):
        super().__init__(master, fg_color="#2B2B2B", *args, **kwargs)
        
        # Setup
        win_ico = ImageTk.PhotoImage(file="interface/assets/info_ico_l.png")
        self.title(title)
        self.wm_iconbitmap()
        self.iconphoto(False, win_ico)
        self.geometry("450x450")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        
        fnt1 = customtkinter.CTkFont(font_name, 16)
        desc = "Esse projeto surgiu da ideia de criar um programa\npara pesquisar livros de forma simples,\nusando a API pública da Open Library.\n\nA proposta é desenvolver uma interface gráfica\nonde seja possível pesquisar livros,\nvisualizar as informações encontradas e\nsalvar os resultados para consultar depois."
        credits = "Wilson Oliveira\n\nGabriel Haua\n\nGabriel de Siqueira\n\nJosyane Almeida\n\nWinicius Santana"
        
        self.lab1 = customtkinter.CTkLabel(self, 
            font=fnt1, 
            text="Descrição :\n\n" + desc + "\n\nCreditos :\n\n" + credits,
        )
        self.lab1.grid(padx=55, pady=25, sticky="se")


# Criar classe da janela de informação do banco de dados.
class DatabaseInfoWindow(customtkinter.CTkToplevel):
    def __init__(self, master, title="Dados", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # Setup
        win_ico = ImageTk.PhotoImage(file="interface/assets/data_ico_l.png")
        self.title(title)
        self.wm_iconbitmap()
        self.iconphoto(False, win_ico)
        self.geometry("400x550")
        self.resizable(False, False)

        #ADICIONADO: Background para a tela de banco de dados
        self.bg_image = customtkinter.CTkImage(
            light_image=Image.open("interface/assets/bg.png"),
            dark_image=Image.open("interface/assets/bg_dark.png"),
            size=(400, 550)
        )
        self.bg_label = customtkinter.CTkLabel(self, text="", image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.grid_columnconfigure(0, weight=1)
        
        fnt1 = customtkinter.CTkFont(font_name, 14)
        # Listas que guardam os dados e os componentes visuais.
        self.book_data_list = []
        self.book_widget_list = []
        
        # Instanciar cabeçalho.
        self.header = HeaderBar(self, type="dataWin")
        self.header.grid(
            row=0,
            column=0,
            padx=0,
            pady=(0, 0),
            sticky="ew"
        )
        
        # Criar um ScrollableFrame, novamente, Esse widget tem problemas de lag.
        self.entryList = customtkinter.CTkScrollableFrame(
            self, 
            height=400, 
            corner_radius=0, 
            label_font = fnt1, 
            label_text="Dados :",
            label_text_color="white",
            label_fg_color="#8BA592",
            border_width=2,
            border_color="#8BA592",
            fg_color=("#ECECEC", "#2B2B2B"),
            scrollbar_button_color="#8BA592",
            scrollbar_button_hover_color="#AECDB6"
        )
        self.entryList.grid(
            row=1,
            column=0,
            padx=30,
            pady=(30, 0),
            sticky="ew"
        )
        
        # Criar botão para limpar o banco de dados.
        self.clearButt = customtkinter.CTkButton(
            self,
            text="Limpar Dados",
            font=fnt1,
            corner_radius=0,
            border_width=1,
            border_color="#ECECEC",
            fg_color="#8BA592",
            hover_color="#AECDB6",
            command=self._clearBank

        )
        self.clearButt.grid(
            row=2,
            column=0,
            padx=120,
            pady=15,
            sticky="ew"
        )
    
    # deleta uma entrada no banco.
    def _deleteEntry(self):
        print("Livro deletado!")
        
    # limpa todos os dados do banco.
    def _clearBank(self):
        print("Banco deletado!")

# Criar classe do cabeçalho da página.
class HeaderBar(customtkinter.CTkFrame):
    def __init__(self, master, type="default", dataWin=None, infoWin=None, **kwargs):
        super().__init__(master, corner_radius=0, height=32, fg_color=("#ECECEC", "#2B2B2B"), **kwargs)
        self.master = master
        self.dataWin = dataWin
        self.infoWin = infoWin

        # Configurar alinhamento.
        self.grid_columnconfigure(0, weight=1)

        if type == "default": 
            # Criar imagem para o ícone de informação.
            info_ico = customtkinter.CTkImage(
                light_image=Image.open("interface/assets/info_ico_d.png"),
                dark_image=Image.open("interface/assets/info_ico_l.png"),
                size=(24, 24)
            )

            # Criar imagem para o ícone de banco de dados.
            data_ico = customtkinter.CTkImage(
                light_image=Image.open("interface/assets/data_ico_d.png"),
                dark_image=Image.open("interface/assets/data_ico_l.png"),
                size=(24, 24)
            )
            
            # Criar botão de informação.
            self.dataButt = customtkinter.CTkButton(
                self,
                image=data_ico,
                text="",
                width=32,
                height=32,
                fg_color="transparent",
                corner_radius=16,
                hover_color=("#ECECEC", "#2B2B2B"),
                command=self._showData
            )
            self.dataButt.grid(row=0, column=0, padx=0, pady=0, sticky="w")
        
            # Criar botão de informação.
            self.infoButt = customtkinter.CTkButton(
                self,
                image=info_ico,
                text="",
                width=32,
                height=32,
                fg_color="transparent",
                corner_radius=16,
                hover_color=("#ECECEC", "#2B2B2B"),
                command=self._showCredits
            )
            self.infoButt.grid(row=0, column=0, padx=0, pady=0, sticky="e")
        else:
            # Criar imagem para o ícone de informação.
            file_ico = customtkinter.CTkImage(
                light_image=Image.open("interface/assets/file_ico_d.png"),
                dark_image=Image.open("interface/assets/file_ico_l.png"),
                size=(24, 24)
            )
            # Criar botão de informação.
            self.filebutt = customtkinter.CTkButton(
                self,
                image=file_ico,
                text="",
                width=32,
                height=32,
                fg_color="transparent",
                corner_radius=16,
                hover_color=("#ECECEC", "#2B2B2B"),
                command=self._selectCSV
            )
            self.filebutt.grid(row=0, column=0, padx=0, pady=0, sticky="w")
            
    # 
    def _selectCSV(self):
        print("Arquivo Aberto!")
    
    # Mostrar uma janela com a descrição e os créditos do projeto.
    def _showCredits(self):
        print("Creditado...")

        if self.infoWin is None or not self.infoWin.winfo_exists():
            self.infoWin = CreditsInfoWindow(self.master)
        else:
            self.infoWin.focus()

    # Criar janela para mostrar o banco de dados, e Focar se já existir.
    def _showData(self):
        if self.dataWin is None or not self.dataWin.winfo_exists():
            self.dataWin = DatabaseInfoWindow(self.master)
        else:
            self.dataWin.focus()

# Criar classe da caixa de pesquisa.
class SearchBar(customtkinter.CTkFrame):
    def __init__(self, master, command):
        super().__init__(master, fg_color=("#ECECEC", "#2B2B2B"))

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
        self.grid_columnconfigure(0, weight=1)

        # Criar botão de pesquisa.
        self.button = customtkinter.CTkButton(
            self,
            image=search_ico,
            font=fnt1,
            text="",
            width=32,
            height=32,
            fg_color="transparent",
            corner_radius=16,
            hover_color=("#ECECEC", "#2B2B2B"),
            command=self._search
        )
        self.button.grid(row=0, column=1, padx=0, pady=0, sticky="e")

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
        self.entry.grid(row=0, column=0, padx=(5, 5), pady=5, sticky="we")

        # Permitir pesquisar apertando Enter.
        self.entry.bind("<Return>", lambda event: self._search())

    # Executar a pesquisa quando o usuário clicar no botão.
    def _search(self):
        titulo = self._getText().strip()

        if titulo != "":
            self.command(titulo)
            self._clearText()
        else:
            messagebox.showwarning(
                "Atenção",
                "Digite o nome de um livro."
            )

    # Apagar o texto do campo de pesquisa.
    def _clearText(self):
        self.entry.delete(0, "end")

    # Retornar o texto digitado.
    def _getText(self):
        return self.entry.get()

# Criar classe dos livros que serão mostrados na interface.
class Book(customtkinter.CTkFrame):
    def __init__(
        self,
        master,
        type="default",
        image="interface/assets/app_ico.png",
        book_name="Livro X",
        author="X",
        r_date="01/01/0000",
        **kwargs
    ):
        super().__init__(
            master,
            bg_color="transparent",
            fg_color=("#ECECEC", "#2B2B2B"),
            border_width=0,
            **kwargs
        )

        fnt1 = customtkinter.CTkFont(font_name, 14)
        fnt2 = customtkinter.CTkFont(font_name, 16)

        # Guardar os dados que serão exibidos.
        self.book_image = ImageTk.PhotoImage(file=image)
        self.book_name = book_name
        self.author_text = "Autor(a) : " + author
        self.r_date_text = "Data de lançamento : " + r_date

        # Configurar alinhamento.
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
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
        self.frame1.grid(row=0, column=1, padx=(25, 0), sticky="nw")

        # Exibir título.
        self.name = customtkinter.CTkLabel(
            self.frame1,
            corner_radius=0,
            bg_color="transparent",
            font=fnt2,
            text=self.book_name,
            anchor="nw"
        )
        self.name.grid(row=0, column=0, padx=0, pady=0, sticky="w")

        # Exibir autor.
        self.author = customtkinter.CTkLabel(
            self.frame1,
            corner_radius=0,
            bg_color="transparent",
            font=fnt1,
            text_color=("#9A9A9A", "#bfbfbf"),
            text=self.author_text,
            anchor="nw"
        )
        self.author.grid(row=1, column=0, padx=0, pady=0, sticky="w")

        # Exibir data de lançamento.
        self.r_date = customtkinter.CTkLabel(
            self.frame1,
            corner_radius=0,
            bg_color="transparent",
            font=fnt1,
            text_color=("#9A9A9A", "#bfbfbf"),
            text=self.r_date_text,
            anchor="nw"
        )
        self.r_date.grid(row=2, column=0, padx=0, pady=0, sticky="w")

        if type == "default":
            # Criar imagem do botão de favoritos.
            img = customtkinter.CTkImage(
                light_image=Image.open("interface/assets/bookmark_ico_d.png"),
                dark_image=Image.open("interface/assets/bookmark_ico_l.png"),
                size=(16, 24)
            )
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
                corner_radius=16,
                hover_color=("#ECECEC", "#2B2B2B"),
                fg_color="transparent",
                bg_color="transparent",
                font=fnt1,
                text="",
                image=img,
                command=self._addBookmark
            )
            self.bookmark.grid(row=0, column=0, padx=0, pady=0, sticky="ne")
        else:
            # Criar imagem do botão de deletar.
            img = customtkinter.CTkImage(
                light_image=Image.open("interface/assets/trash_ico_d.png"),
                dark_image=Image.open("interface/assets/trash_ico_l.png"),
                size=(16, 24)
            )
            # Criar quadro do botão de deletar.
            self.frame2 = customtkinter.CTkFrame(
                self,
                corner_radius=0,
                fg_color="transparent"
            )
            self.frame2.grid(row=0, column=2, sticky="ne")
            # Criar botão de deletar.
            self.bookmark = customtkinter.CTkButton(
                self.frame2,
                width=32,
                height=32,
                corner_radius=16,
                hover_color=("#ECECEC", "#2B2B2B"),
                fg_color="transparent",
                bg_color="transparent",
                font=fnt1,
                text="",
                image=img,
                command=self._deleteEntry
            )
            self.bookmark.grid(row=0, column=0, padx=0, pady=0, sticky="ne")
        
    def _deleteEntry():
        pass
    
    # Adicionar o livro aos favoritos.
    def _addBookmark(self):
        print("Bookmarked : " + self.book_name)

        # Fazer mais coisas aqui futuramente.

# Criar classe do painel que mostra os resultados da pesquisa.
class Results(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            label_text="Resultados :",
            label_font = customtkinter.CTkFont(font_name, 14),
            label_text_color="white",
            label_fg_color="#8BA592",
            border_width=2,
            border_color="#8BA592",
            fg_color=("#ECECEC", "#2B2B2B"),
            scrollbar_button_color="#8BA592",
            scrollbar_button_hover_color="#AECDB6",
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
    def _refresh(self):
        for widget in self.book_widget_list:
            widget.destroy()

        self.book_widget_list = []
        self.book_data_list = []

    # Pesquisar livros na API e mostrar os resultados.
    def buscar(self, titulo):
        self._refresh()

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

        # Configurações da janela.
        self.title(title)
        self.iconbitmap("interface/assets/app_task_ico.ico")
        self.geometry(geometry)
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)

        #ADICIONADO: background
        self.bg_image = customtkinter.CTkImage(
            light_image=Image.open("interface/assets/bg.png"),
            dark_image=Image.open("interface/assets/bg_dark.png"),
            size=(540, 700)
        )
        self.bg_label = customtkinter.CTkLabel(self, text="", image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        fnt1 = customtkinter.CTkFont(font_name, 14)
        self.dataWin = None

        # Instanciar cabeçalho.
        self.header = HeaderBar(self, "default", dataWin=self.dataWin)
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
            pady=(20, 18),
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
            font=fnt1,
            command=self.results.exportar,
            corner_radius=0,
            border_width=1,
            border_color="#ECECEC",
            fg_color="#8BA592",
            hover_color="#AECDB6"
        )
        self.export_button.grid(
            row=3,
            column=0,
            padx=180,
            pady=(0, 20),
            sticky="ew"
        )

# Ponto de entrada do aplicativo.
# Execute main.py para iniciar a aplicação.