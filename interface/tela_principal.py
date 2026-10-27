# Importar bibliotecas usadas para a interface gráfica.
from CTkMessagebox import CTkMessagebox
import customtkinter
# Importar a biblioteca "Pillow" para utilizar imagens na interface gráfica.
from PIL import (Image, ImageTk)

#region Misc :

font_name = "Georgia"

#endregion

#region Classes :

# Criar classe do header da página.
class HeaderBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=0, height=32, **kwargs)
        
        # Criar imagem para o ícone de informação.
        info_ico = customtkinter.CTkImage(
            light_image=Image.open("interface/assets/info_ico_d.png"),
            dark_image=Image.open("interface/assets/info_ico_l.png"),
            size=(24, 24))
        
        # Configurar alinhamento.
        self.grid_columnconfigure(0, weight=1)
        
        # Criar os widgets da caixa de procura.
        self.button = customtkinter.CTkButton(self, image=info_ico, text="", width=32, height=32, fg_color="transparent", corner_radius=0, hover_color="#404040", command=self.btn_callback)
        self.button.grid(row=0, column=0, padx=0, pady=0, sticky="e")
    
    # Mostra um Alert contendo uma descrição do projeto e os créditos dos desenvolvedores.
    def btn_callback(self):
        # Adicionar a descrição e créditos.
        print("Creditado...")
        fnt1 = customtkinter.CTkFont(font_name, 14)
        CTkMessagebox(master=app, corner_radius=0, font=fnt1, title="Descrição.", message="Descrição do projeto :\n\nCréditos :", icon="interface/assets/info_ico_l.png", header=True)

# Criar classe de caixa de procura.
class SearchBar(customtkinter.CTkFrame):
    def __init__(self, master, command):
        super().__init__(master, fg_color="transparent")
        
        # Criar fonte para a caixa de procura.
        fnt1 = customtkinter.CTkFont(font_name, 16)
        
        # Criar imagem para o ícone de procura.
        search_ico = customtkinter.CTkImage(
            light_image=Image.open("interface/assets/search_ico_d.png"),
            dark_image=Image.open("interface/assets/search_ico_l.png"),
            size=(24, 24))

        self.command = command

        # Configurar alinhamento.
        self.grid_columnconfigure(0, weight=1)
        
        # Criar os widgets da caixa de procura.
        self.button = customtkinter.CTkButton(self, image=search_ico, font=fnt1, text="", width=32, height=32, fg_color="transparent", corner_radius=8, hover_color="#404040", command=self.btn_callback)
        self.button.grid(row=0, column=0, padx=0, pady=0, sticky="w")
        self.entry = customtkinter.CTkEntry(self, font=fnt1, placeholder_text="Digite o nome do livro desejado aqui.", width=332, height=32, corner_radius=0, fg_color="transparent")
        self.entry.grid(row=0, column=1, padx=(0, 5), pady=5, sticky="we")
    
    # Callback.
    def btn_callback(self):
        if self.get_text() != "":
            print(self.get_text())
            self.reset_text()
            self.command()
    
    # Reset o texto da caixa de procura.
    def reset_text(self):
        if self.get_text() != "":
            self.entry.set("")
        
    # Retorna o texto da caixa de procura
    def get_text(self):
        return self.entry.get()

# Criar classe dos livros que serão mostrados.
class Book(customtkinter.CTkFrame):
    def __init__(self, master, image="interface/assets/app_ico.png", book_name="Livro X", author="X", r_date="01/01/0000", **kwargs):
        super().__init__(master, bg_color = "transparent", border_width=0, **kwargs)
        
        fnt1 = customtkinter.CTkFont(font_name, 14)
        fnt2 = customtkinter.CTkFont(font_name, 16)
        
        bookmark_image = customtkinter.CTkImage(
            light_image=Image.open("interface/assets/bookmark_ico_d.png"),
            dark_image=Image.open("interface/assets/bookmark_ico_l.png"),
            size=(16, 24))
        
        self.image = ImageTk.PhotoImage(file=image)
        self.book_name = book_name
        self.author = "Autor(a) : " + author
        self.r_date = "Data de lançamento : " + r_date
        
        # Configuração :
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=0)
        
        # Widgets :
        self.image = customtkinter.CTkLabel(self, corner_radius=0, bg_color="transparent", font=fnt2, text="", image=self.image, anchor="nw")
        self.image.grid(row=0, column=0, padx=(20, 0), pady=0, sticky="nw")
        
        self.frame1 = customtkinter.CTkFrame(self, width=128, height=128, corner_radius=0, fg_color="transparent")
        self.frame1.grid(row=0, column=1, sticky="nw")
        
        self.name = customtkinter.CTkLabel(self.frame1, corner_radius=0, bg_color="transparent", font=fnt2, text=self.book_name, anchor="nw")
        self.name.grid(row=0, column=0, padx=0, pady=0, sticky="nw")
        
        self.author = customtkinter.CTkLabel(self.frame1, corner_radius=0, bg_color="transparent", font=fnt1, text_color="#bfbfbf", text=self.author, anchor="nw")
        self.author.grid(row=1, column=0, padx=0, pady=0, sticky="nw")
                
        self.r_date = customtkinter.CTkLabel(self.frame1, corner_radius=0, bg_color="transparent", font=fnt1, text_color="#bfbfbf", text=self.r_date, anchor="nw")
        self.r_date.grid(row=2, column=0, padx=0, pady=0, sticky="nw")
        
        self.frame2 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame2.grid(row=0, column=2, sticky="ne")
        
        self.bookmark = customtkinter.CTkButton(self.frame2, width=32, height=32, corner_radius=8, hover_color="#404040", fg_color="transparent" , bg_color="transparent", font=fnt1, text="", image=bookmark_image, command=self.btn_callback)
        self.bookmark.grid(row=0, column=0, padx=0, pady=0, sticky="ne")
    
    def btn_callback(self):
        self.add_bookmark()
        # Fazer mais coisas aqui!!!
    
    # Retorna os dados do livro.
    def get_data(self):
        pass
    
    # Adiciona esse livro ao bookmark.
    def add_bookmark(self):
        print("Bookmarked : " + self.book_name)
        # Fazer mais coisas aqui!!!

# Criar classe do painel que mostra os resultados da pesquisa.
class Results(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, label_text="Resultados :", corner_radius=0, height=400,**kwargs)
        
        # ScrollableFrame Widget tem um problema de lag.
        # https://github.com/TomSchimansky/CustomTkinter/issues/215
        # Podemos usar o Widget ScrollBar e Frame do TKinter original, pelo que eu vi, ele não tem esse problema.
        # Por enquanto eu decidi focar em outras coisas.
        
        # Configuração :
        self.grid_columnconfigure((0), weight=1)
        
        # Widgets :
        self.book_data_list = []
        self.book_widget_list = []
        
        # Usando valores estáticos para testes.
        for i in range(10):
            book = Book(self, book_name="Livro " + str(i + 1), author="Autor " + str(i + 1))
            book.grid(row=i, column=0, padx=5, pady=(15, 5), sticky="we")
            
            self.book_widget_list.append(book)
    
    # Reiniciar os resultados.
    def refresh(self):
        if len(self.book_widget_list) > 0:
            for i, v in enumerate(self.book_widget_list):
                self.book_widget_list[i].destroy()
        self.book_widget_list = []
        self.book_widget_list = []
    
    # Update dos resultados.
    def update(self):
        self.refresh()
        # Fazer mais coisas aqui!!!

# Criar classe principal do aplicativo.
class App(customtkinter.CTk):
    def __init__(self, title = "Nome do Programa", geometry="540x648", fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        app_ico = ImageTk.PhotoImage(file="interface/assets/app_ico.png")
        
        # Configuração :
        self.title(title)
        self.wm_iconbitmap()
        self.iconphoto(False, app_ico)
        self.geometry(geometry)
        self.resizable(False, False)
        self.grid_columnconfigure((0), weight=1)
        #self.grid_rowconfigure(0, weight=1)
        
        # Widgets :
        # Instanciar header.
        self.header = HeaderBar(self)
        # Aplicar alinhamento.
        self.header.grid(row=0, column=0, padx=0, pady=(0, 0), sticky="ew")
        
        # Instanciar resultados.
        self.results = Results(self)
        # Aplicar alinhamento.
        self.results.grid(row=2, column=0, padx=40, pady=(20, 40), sticky="nsew")
        
        # Instanciar caixa de procura.
        self.searchBar = SearchBar(self, self.results.update)
        # Aplicar alinhamento.
        self.searchBar.grid(row=1, column=0, padx=80, pady=(40, 20), sticky="ew")
            

#endregion

# Criar instancia da classe App.
app = App("Nome do Programa", "540x648")
# Iniciar Loop principal da interface gráfica.
app.mainloop()