import customtkinter as ctk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraficoPage(ctk.CTkToplevel):
    """
   TopLevel que exibe gráficos de MRU ou MRUV em abas.

    MRU  → receber v e t é suficiente (a = 0 fixo)
    MRUV → usa os valores brutos + dicionário de calculados
    
    """
    
    def __init__(self, master, modo: str ,s0=None, s=None, v0=None, v=None, a=None, t=None, calculados: dict = {}):
        super().__init__(master)

        self.title(f"Gráficos - {modo.upper()}")
        self.geometry("720x520")
        self.after(250, lambda: self.iconbitmap("assets/icon-ico/grafico-icon.ico"))
        self.attributes("-topmost", True)
        self.after(100, self.lift)
        self.after(100, self.focus_force)

        self.modo = modo.upper()

        # --- Resolve valores ---
        if self.modo == "MRU":
            self.t_val  = t
            self.v0_val = v   # no MRU velocidade é constante
            self.v_val  = v
            self.a_val  = 0.0 # aceleração sempre zero no MRU
            self.s0_val = s0 if s0 is not None else 0.0

        else:  # MRUV
            self.t_val  = t  or calculados.get("Tempo (t)")
            self.v0_val = v0 or calculados.get("Vel. Inicial (pelo tempo)") \
                             or calculados.get("Vel. Inicial (distância)")
            self.v_val  = v  or calculados.get("Velocidade Final (v)")
            self.a_val  = a  or calculados.get("Aceleração (pelo tempo)") \
                             or calculados.get("Aceleração (Torricelli)")
            self.s0_val = s0 if s0 is not None else 0.0

        self._build_ui()

    def _build_ui(self):
        if self.t_val is None:
            ctk.CTkLabel(self, text="Sem valor de tempo para gerar gráficos.",
                         text_color="red").pack(expand=True)
            return

        tabview = ctk.CTkTabview(self, corner_radius=12)
        tabview.pack(fill="both", expand=True, padx=10, pady=10)

        tempo = np.linspace(0, self.t_val, 300)
        abas_criadas = 0

        # --- s x t ---
        if self.v0_val is not None and self.a_val is not None:
            tabview.add("s x t")
            posicao = self.s0_val + self.v0_val * tempo + 0.5 * self.a_val * tempo**2
            self._plotar(tabview.tab("s x t"), tempo, posicao,
                         xlabel="Tempo (s)", ylabel="Posição (m)",
                         titulo="Posição x Tempo", cor="#7c9ef5")
            abas_criadas += 1

        # --- v x t ---
        if self.v0_val is not None and self.a_val is not None:
            tabview.add("v x t")
            velocidade = self.v0_val + self.a_val * tempo  # MRU: a=0, fica constante
            self._plotar(tabview.tab("v x t"), tempo, velocidade,
                         xlabel="Tempo (s)", ylabel="Velocidade (m/s)",
                         titulo="Velocidade x Tempo", cor="#f5a97f")
            abas_criadas += 1

        # --- a x t ---
        if self.a_val is not None:
            tabview.add("a x t")
            aceleracao = np.full_like(tempo, self.a_val)  # MRU: linha em zero
            self._plotar(tabview.tab("a x t"), tempo, aceleracao,
                         xlabel="Tempo (s)", ylabel="Aceleração (m/s²)",
                         titulo="Aceleração x Tempo", cor="#a6e3a1",
                         linestyle="--")
            abas_criadas += 1

        if abas_criadas == 0:
            ctk.CTkLabel(self, text="Dados insuficientes para gerar gráficos.",
                         text_color="red").pack(expand=True)
            tabview.destroy()
    
    def _plotar(self, aba, x, y, xlabel, ylabel, titulo, cor, linestyle="-"):
       
        """Cria e embute um gráfico matplotlib dentro de uma aba."""
        fig = Figure(figsize=(6, 4), dpi=100)
        ax  = fig.add_subplot(111)

        ax.plot(x, y, color=cor, linewidth=2, linestyle=linestyle)

        ax.set_facecolor("#1e1e2e")
        fig.patch.set_facecolor("#1e1e2e")
        ax.set_xlabel(xlabel, color="white")
        ax.set_ylabel(ylabel, color="white")
        ax.set_title(titulo, color="white", fontsize=13)
        ax.tick_params(colors="white")
        ax.grid(color="#333355", linestyle="--", linewidth=0.5)
        for spine in ax.spines.values():
            spine.set_edgecolor("#555577")

        canvas = FigureCanvasTkAgg(fig, master=aba)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)