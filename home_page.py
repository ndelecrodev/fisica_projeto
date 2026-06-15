import customtkinter as ctk

class HomePage(ctk.CTkFrame):
    """
    Primeira página da aplicação, menu principal de seleção de conteúdo.
    Recebe um callback 'on_navigate' para trocar de página sem depender do Home.
    """

    def __init__(self, master, on_navigate: callable):
        super().__init__(master)
        self.on_navigate = on_navigate
        self._build_ui()

    def _build_ui(self):

        ctk.CTkLabel(self, text="Aperte o botão de sua escolha:", text_color="cyan", font=("Arial", 20, "bold")).pack(pady=50, padx=20)
        b_mru_mruv = ctk.CTkButton(self, text="MRU e MRUV", command=lambda: self.on_navigate("mru_mruv"), height=42, width=200, font=("Arial", 15, "bold"), text_color="white")
        b_mru_mruv.pack(pady=50, padx=20)
        b_outro_conteudo1 = ctk.CTkButton(self, text="Outro conteúdo", height=42, width=200, font=("Arial", 15, "bold"), text_color="white")
        b_outro_conteudo1.pack(pady=50, padx=20)
        b_outro_conteudo2 = ctk.CTkButton(self, text="Outro conteúdo", width=200, height=42, font=("Arial", 15, "bold"), text_color="white")
        b_outro_conteudo2.pack(pady=50, padx=20)
        b_outro_conteudo3 = ctk.CTkButton(self, text="Outro conteúdo", width=200, height=42, font=("Arial", 15, "bold"), text_color="white")
        b_outro_conteudo3.pack(pady=50, padx=20)