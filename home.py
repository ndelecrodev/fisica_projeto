import customtkinter as ctk
from home_page import HomePage
from page_mru_mruv import MruMruvPage

# Variaveis que começam com b são botões 
# Variaveis que começam com e são entrys(entradas)
# Variaveis que começam com l são labels(texto)

titulos = {
    "inicial": "Física - Home Page",
    "mru_mruv": "Física - Mru Mruv",
}


class Home(ctk.CTk):
    """
    Janela raiz: registra todas as páginas e controla qual está visível.
    Adicionar uma nova página = instanciá-la aqui e mapear no dicionário.
    """
     
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.after(0, lambda:self.state("zoomed"))

        
        # Registra paginas

        self._paginas: dict[str, ctk.CTkFrame] = {
            "inicial": HomePage(self, on_navigate=self.browse),
            "mru_mruv": MruMruvPage(self, on_navigate=self.browse),
        }

        # Exibe a pagina de entrada

        self.browse("inicial")
    
    def browse(self, destination: str):
        """
        Esconde todas as páginas e exibe apenas `destino`.
        Também atualiza o título da janela e o favicon.
        """
        if destination not in self._paginas:
            raise KeyError(f"Página Desconhecida: 'Destino: {destination}'")
        
        for pagina in self._paginas.values():
            pagina.pack_forget()
        
        self._paginas[destination].pack(fill="both", expand=True)
        self.title(titulos.get(destination, "Física"))
        if destination == "inicial":
            self.iconbitmap(destination, "assets/icon-ico/pagina-inicial.ico")
        elif destination == "mru_mruv":
            self.iconbitmap(destination, "assets/icon-ico/mru-e-mruv.ico")

# inicializando a pagina inicial

app = Home()
app.mainloop()
