import customtkinter as ctk
from mru import Mru
from mruv import Mruv
from grafico_mru_mruv import GraficoPage

class MruMruvPage(ctk.CTkFrame):
    """
    Segunda página — calculadora de MRU e MRUV com abas (TabView).
    Recebe um callback `on_navigate` para navegação e
    reutiliza os diálogos de resultado/erro definidos aqui mesmo.

    """
    def __init__(self, master, on_navigate: callable):
        super().__init__(master)
        self.on_navigate = on_navigate
        self._build_ui()

        # Construção da ainterface 
        
    def _build_ui(self):

        tabview = ctk.CTkTabview(self, corner_radius=20, width=700)
        tabview.pack(pady=5)

        tabview.add("MRU")
        tabview.add("MRUV")
        tabview.tab("MRU").grid_columnconfigure(0, weight=1)
        tabview.tab("MRUV").grid_columnconfigure(0, weight=1)

        self._build_aba_mru(tabview.tab("MRU"))
        self._build_aba_mruv(tabview.tab("MRUV"))

    def _build_aba_mru(self, tab):
        self._tab_mru = tab
        self.check_var1 = ctk.BooleanVar(value=False)
        self.check_var2 = ctk.BooleanVar(value=False)
        
        self.check_var3 = ctk.BooleanVar(value=False)
        self.check_var4 = ctk.BooleanVar(value=False)

        ctk.CTkLabel(tab, text="OBS: escolha somente uma opção", font=("Arial", 12), text_color="red").pack(pady=8)

        ctk.CTkLabel(tab, text="Escolha o que você deseja calcular:", font=("Arial", 15)).pack(pady=8)
        
        box1 = ctk.CTkCheckBox(tab, text="Calcular Posição Final (s)", border_width=1, border_color="white", variable=self.check_var1, command=self.checkBoxesMru).pack(pady=8)

        box2 = ctk.CTkCheckBox(tab, text="Calcular Velocidade (v)", border_width=1, border_color="white", variable=self.check_var2, command=self.checkBoxesMru).pack(pady=8)

        box3 = ctk.CTkCheckBox(tab, text="Calcular Tempo (t)", border_width=1, border_color="white", variable=self.check_var3, command=self.checkBoxesMru).pack(pady=8)

        self.t_ds = ctk.CTkLabel(tab, text="Você possui o Espaço Percorrido (\u0394s)?")

        self.box4 = ctk.CTkCheckBox(tab, text="Sim", border_width=1, border_color="white", variable=self.check_var4, command=self.checkBoxesMru)

        self.t_delta_s = ctk.CTkLabel(tab, text="Digite o Espaço Percorrido (\u0394s):")
        self.entry_d = ctk.CTkEntry(tab, placeholder_text="Digite o \u0394s")
        self.t_s = ctk.CTkLabel(tab, text="Posição Final:")
        self.entry_sf = ctk.CTkEntry(tab, placeholder_text="Digite a posição final")
        self.t_pi = ctk.CTkLabel(tab, text="Posição Inicial:")
        self.entry_s0 = ctk.CTkEntry(tab, placeholder_text="Digite a posição inicial")
        self.t_vc = ctk.CTkLabel(tab, text="Velocidade: ")
        self.entry_v = ctk.CTkEntry(tab, placeholder_text="Digite a velocidade")
        self.t_t = ctk.CTkLabel(tab, text="Tempo:")
        self.entry_t = ctk.CTkEntry(tab, placeholder_text="Digite o tempo")
        self.b_mru = ctk.CTkButton(tab, text="Calcular", command=self.calcularMru)
        self.b_voltar_mru = ctk.CTkButton(tab, text="Voltar", command= lambda: self.on_navigate("inicial"))
        self.b_voltar_mru.pack(pady=5)
    
    def _build_aba_mruv(self, tab):
        self._tab_mruv = tab
        scroll = ctk.CTkScrollableFrame(tab, width=800, height=600)
        scroll.pack(fill="both", expand=True, padx=5, pady=5)
        self.checar_box_mruv1 = ctk.BooleanVar(value=False)
        self.checar_box_mruv2 = ctk.BooleanVar(value=False)
        ctk.CTkLabel(scroll, text="OBS: se não tiver o valor pedido não coloque nada nas caixas de texto, digite as medidas de distancia em metros, tempo em segundos, e aceleração em m/s²", text_color="red", font=("Arial", 12)).pack(pady=3)
        ctk.CTkLabel(scroll, text="Você possui o Espaço Percorrido para calculo? Assine somente uma opção:", font=("Arial", 15)).pack(pady=5)
        check_box_mruv1 = ctk.CTkCheckBox(scroll, text="Sim", border_width=1, border_color="white", variable=self.checar_box_mruv1, command=self.checkBoxesMruv)
        check_box_mruv1.pack(pady=10)
        check_box_mruv2 = ctk.CTkCheckBox(scroll, text="Não", border_width=1, border_color="white", variable=self.checar_box_mruv2, command=self.checkBoxesMruv)
        check_box_mruv2.pack(pady=10)
        self.t_ep = ctk.CTkLabel(scroll, text="Espaço Percorrido: ")
        self.entry_ep = ctk.CTkEntry(scroll, placeholder_text="Digite o Espaço Percorrido")        
        self.t_pi_mruv = ctk.CTkLabel(scroll, text="Posição Inicial: ")
        self.entry_s02 = ctk.CTkEntry(scroll, placeholder_text="Digite a posição inicial")
        self.t_pf = ctk.CTkLabel(scroll, text="Posição Final: ")
        self.entry_s2 = ctk.CTkEntry(scroll, placeholder_text="Digite a posição final")
        self.t_vi = ctk.CTkLabel(scroll, text="Velocidade Inicial:")
        self.entry_v0 = ctk.CTkEntry(scroll, placeholder_text="Digite a velocidade inicial")
        self.t_vf = ctk.CTkLabel(scroll, text="Velocidade Final:")
        self.entry_vf = ctk.CTkEntry(scroll, placeholder_text="Digite a veloidade final")
        self.t_a_mruv = ctk.CTkLabel(scroll, text="Aceleração: ")
        self.entry_a = ctk.CTkEntry(scroll, placeholder_text="Digite a acelereção")
        self.t_t_mruv = ctk.CTkLabel(scroll, text="Digite o tempo: ")
        self.entry_t2 = ctk.CTkEntry(scroll, placeholder_text="Digite o tempo")
        self.b_mruv = ctk.CTkButton(scroll, text="Calcular", command=self.calcularMruv)
        self.b_voltar_mruv = ctk.CTkButton(scroll, text="Voltar", command= lambda: self.on_navigate("inicial"))
        self.b_voltar_mruv.pack(pady=5)

    def checkBoxesMru(self):
        
        for entry in [self.entry_s0, self.entry_v, self.entry_t,
                  self.entry_sf, self.entry_d]:
            entry.unbind("<Return>")
        try:
            entry._entry.unbind("<Return>")
        except AttributeError:
            pass

        if self.check_var1.get() == True and self.check_var2.get() == False and self.check_var3.get() == False:
            self.box4.pack_forget()
            self.b_mru.pack_forget()
            self.b_voltar_mru.pack_forget()
            self.t_s.pack_forget()
            self.entry_sf.pack_forget()
            self.t_pi.pack(pady=5)
            self.entry_s0.pack(pady=5)
            self.t_vc.pack(pady=5)
            self.entry_v.pack(pady=5)
            self.t_t.pack(pady=5)
            self.entry_t.pack(pady=5)
            self.b_mru.pack(pady=5)
            self.b_voltar_mru.pack(pady=5)

            self._bind_entry_return(self.entry_s0, self.calcularMru)
            self._bind_entry_return(self.entry_v,  self.calcularMru)
            self._bind_entry_return(self.entry_t,  self.calcularMru)

        elif self.check_var1.get() == False and self.check_var2.get() == True and self.check_var3.get() == False:
            self.t_ds.pack(pady=5)
            self.box4.pack(pady=6)

            if self.check_var4.get() == True:
                self.entry_s0.pack_forget()
                self.t_pi.pack_forget()
                self.t_s.pack_forget()
                self.entry_sf.pack_forget()
                self.b_mru.pack_forget()
                self.b_voltar_mru.pack_forget()
                self.t_delta_s.pack(pady=6)
                self.entry_d.pack(pady=8)
                self.t_t.pack(pady=5)
                self.entry_t.pack(pady=8)
                self.b_mru.pack(pady=5)
                self.b_voltar_mru.pack(pady=5)

            elif self.check_var4.get() == False:
                self.t_delta_s.pack_forget()
                self.entry_d.pack_forget()
                self.b_mru.pack_forget()
                self.b_voltar_mru.pack_forget()
                self.t_t.pack(pady=7)
                self.entry_t.pack(pady=6)
                self.t_pi.pack(pady=5)
                self.entry_s0.pack(pady=5)
                self.t_s.pack(pady=5)
                self.entry_sf.pack(pady=5)
                self.b_mru.pack(pady=5)
                self.b_voltar_mru.pack(pady=5)

            self._bind_entry_return(self.entry_s0,  self.calcularMru)
            self._bind_entry_return(self.entry_v,   self.calcularMru)
            self._bind_entry_return(self.entry_sf,  self.calcularMru)
            self._bind_entry_return(self.entry_d,   self.calcularMru)
            self._bind_entry_return(self.entry_t,   self.calcularMru)

        elif self.check_var1.get() == False and self.check_var2.get() == False and self.check_var3.get() == True:
            self.t_ds.pack(pady=5)
            self.box4.pack(pady=6)

            if self.check_var4.get() == True:
                self.t_pi.pack_forget()
                self.t_s.pack_forget()
                self.entry_s0.pack_forget()
                self.entry_sf.pack_forget()
                self.b_mru.pack_forget()
                self.b_voltar_mru.pack_forget()
                self.t_delta_s.pack(pady=6)
                self.entry_d.pack(pady=8)
                self.t_vc.pack(pady=5)
                self.entry_v.pack(pady=8)
                self.b_mru.pack(pady=5)
                self.b_voltar_mru.pack(pady=5)

            elif self.check_var4.get() == False:
                self.t_delta_s.pack_forget()
                self.entry_d.pack_forget()
                self.b_mru.pack_forget()
                self.b_voltar_mru.pack_forget()
                self.t_t.pack_forget()
                self.entry_t.pack_forget()
                self.t_pi.pack(pady=5)
                self.entry_s0.pack(pady=5)
                self.t_vc.pack(pady=5)
                self.entry_v.pack(pady=5)
                self.t_s.pack(pady=5)
                self.entry_sf.pack(pady=5)
                self.b_mru.pack(pady=5)
                self.b_voltar_mru.pack(pady=5)

            self._bind_entry_return(self.entry_s0,  self.calcularMru)
            self._bind_entry_return(self.entry_v,   self.calcularMru)
            self._bind_entry_return(self.entry_sf,  self.calcularMru)
            self._bind_entry_return(self.entry_d,   self.calcularMru)
            self._bind_entry_return(self.entry_v,   self.calcularMru)

        else:
            self.t_ds.pack_forget()
            self.t_delta_s.pack_forget()
            self.box4.pack_forget()
            self.entry_d.pack_forget()
            self.b_mru.pack_forget()
            self.b_voltar_mru.pack_forget()
            self.t_s.pack_forget()
            self.entry_sf.pack_forget()
            self.t_pi.pack_forget()
            self.entry_s0.pack_forget()
            self.t_vc.pack_forget()
            self.entry_v.pack_forget()
            self.t_t.pack_forget()
            self.entry_t.pack_forget()
            self.t_s.pack_forget()
            self.entry_sf.pack_forget()
            self.b_voltar_mru.pack(pady=5)
            self._tab_mru.unbind("<Return>")

   
    def checkBoxesMruv(self):

        for entry in [self.entry_ep, self.entry_s02, self.entry_s2,
                  self.entry_v0, self.entry_vf, self.entry_a, self.entry_t2]:
            entry.unbind("<Return>")

        if self.checar_box_mruv1.get() == True and self.checar_box_mruv2.get() == False:
            self.b_mruv.pack_forget()
            self.b_voltar_mruv.pack_forget()
            self.t_ep.pack(pady=5)
            self.entry_ep.pack(pady=5)
            self.t_pi_mruv.pack(pady=5)
            self.entry_s02.pack(pady=5)
            self.t_pf.pack(pady=5)
            self.entry_s2.pack(pady=5)
            self.t_vi.pack(pady=5)
            self.entry_v0.pack(pady=5)
            self.t_vf.pack(pady=5)
            self.entry_vf.pack(pady=5)
            self.t_a_mruv.pack(pady=5)
            self.entry_a.pack(pady=5)
            self.t_t_mruv.pack(pady=5)
            self.entry_t2.pack(pady=10)
            self.b_mruv.pack(pady=5)
            self.b_voltar_mruv.pack(pady=5)

            self.entry_ep.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_s02.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_s2.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_v0.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_vf.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_a.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_t2.bind("<Return>", lambda event: self.calcularMruv())
            
        elif self.checar_box_mruv1.get() == False and self.checar_box_mruv2.get() == True:
            self.t_ep.pack_forget()
            self.entry_ep.pack_forget()
            self.b_mruv.pack_forget()
            self.b_voltar_mruv.pack_forget()
            self.t_pi_mruv.pack(pady=5)
            self.entry_s02.pack(pady=5)
            self.t_pf.pack(pady=5)
            self.entry_s2.pack(pady=5)
            self.t_vi.pack(pady=5)
            self.entry_v0.pack(pady=5)
            self.t_vf.pack(pady=5)
            self.entry_vf.pack(pady=5)
            self.t_a_mruv.pack(pady=5)
            self.entry_a.pack(pady=5)
            self.t_t_mruv.pack(pady=5)
            self.entry_t2.pack(pady=10)
            self.b_mruv.pack(pady=5)
            self.b_voltar_mruv.pack(pady=5)

            self.entry_s02.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_s2.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_v0.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_vf.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_a.bind("<Return>", lambda event: self.calcularMruv())
            self.entry_t2.bind("<Return>", lambda event: self.calcularMruv())
            
        elif self.checar_box_mruv1.get() == True and self.checar_box_mruv2.get() == True:
            self.t_ep.pack_forget()
            self.entry_ep.pack_forget()
            self.b_mruv.pack_forget()
            self.b_voltar_mruv.pack_forget()
            self.t_pi_mruv.pack_forget()
            self.entry_s02.pack_forget()
            self.t_pf.pack_forget()
            self.entry_s2.pack_forget()
            self.t_vi.pack_forget()
            self.entry_v0.pack_forget()
            self.t_vf.pack_forget()
            self.entry_vf.pack_forget()
            self.t_a_mruv.pack_forget()
            self.entry_a.pack_forget()
            self.t_t_mruv.pack_forget()
            self.entry_t2.pack_forget()
            self.b_mruv.pack_forget()
            self.b_voltar_mruv.pack(pady=10)
        
        elif self.checar_box_mruv2.get() == False and self.checar_box_mruv1.get() == False:
            self.t_ep.pack_forget()
            self.entry_ep.pack_forget()
            self.b_mruv.pack_forget()
            self.b_voltar_mruv.pack_forget()
            self.t_pi_mruv.pack_forget()
            self.entry_s02.pack_forget()
            self.t_pf.pack_forget()
            self.entry_s2.pack_forget()
            self.t_vi.pack_forget()
            self.entry_v0.pack_forget()
            self.t_vf.pack_forget()
            self.entry_vf.pack_forget()
            self.t_a_mruv.pack_forget()
            self.entry_a.pack_forget()
            self.t_t_mruv.pack_forget()
            self.entry_t2.pack_forget()
            self.b_mruv.pack_forget()
            self.b_voltar_mruv.pack(pady=15) 
            self._tab_mruv.bind("<Return>", lambda event: self.calcularMruv())

    def _dialog_resposta_mru(self, resposta: float, nome: str, s0=0.0, v=0.0, t=0.0):
        janela = self._top_level_settings("Resposta MRU", "300x150", "assets/icon-ico/icon_certo_final.ico")
        ctk.CTkLabel(janela, text=f"{nome}: {resposta:.2f}", text_color="green").place(relx=0.5, rely=0.5, anchor="center")
        ctk.CTkButton(janela, text="Ver Gráficos", command= lambda: GraficoPage(self, modo="mru", s0=s0, v=v, t=t)).pack(pady=20)
        janela.bind("<Return>", lambda event: GraficoPage(self, modo="mru", s0=s0, v=v, t=t))
        janela.after(60_000, janela.destroy)

    def _dialog_erro(self, erro: str):
        janela = self._top_level_settings("Erro", "340x150", "assets/icon-ico/png-errado-icon.ico")
        ctk.CTkLabel(janela, text=erro, text_color="red").place(relx=0.5, rely=0.5, anchor="center")
        janela.after(10000, janela.destroy)

    def calcularMru(self):

        try:

                if self.check_var1.get():
                        entry_mru_s0 = float(self.entry_s0.get().strip())
                        entry_mru_v = float(self.entry_v.get().strip())
                        entry_mru_t = float(self.entry_t.get().strip())
                        resultado = Mru(entry_mru_s0, entry_mru_v,).calcularPosicaoFinal(entry_mru_t)
                        self._dialog_resposta_mru(Mru().calcularPosicaoFinal(t=entry_mru_t, s0=entry_mru_s0, v=entry_mru_v), "Posição Final", s0=entry_mru_s0, v=entry_mru_v, t=entry_mru_t)
                        self.entry_t.delete(0,"end")
                        self.entry_v.delete(0,"end")
                        self.entry_s0.delete(0,"end")

                elif self.check_var2.get():
                        if self.check_var4.get():
                            entry_mru_t = float(self.entry_t.get().strip())
                            entry_delta = float(self.entry_d.get().strip())
                            resultado = Mru().calcular_velocidade_espaco(entry_delta, entry_mru_t)
                            self._dialog_resposta_mru(resultado, "Velocidade(v)", v=resultado, t=entry_mru_t)
                            self.entry_v.delete(0,"end")
                            self.entry_d.delete(0,"end") 
                        else:
                            entry_mru_t = float(self.entry_t.get().strip())
                            entry_mru_s0 = float(self.entry_s0.get().strip())
                            entry_mru_s = float(self.entry_sf.get().strip())
                            resultado = Mru().calcular_velocidade(entry_mru_s0, entry_mru_t, entry_mru_s)
                            self._dialog_resposta_mru(resultado, "Velocidade(v)", s0=entry_mru_s0, v=resultado, t=entry_mru_t)
                            self.entry_t.delete(0,"end")
                            self.entry_s0.delete(0,"end")
                            self.entry_sf.delete(0,"end")
                        
                elif self.check_var3.get():
                    if self.check_var4.get():
                        entry_mru_v = float(self.entry_v.get().strip())
                        entry_delta = float(self.entry_d.get().strip())
                        resultado = Mru().calcular_tempo_espaco(entry_delta, entry_mru_v)
                        self._dialog_resposta_mru(resultado, "Tempo(t)", v=entry_mru_v, t=resultado)
                        self.entry_v.delete(0,"end")
                        self.entry_d.delete(0,"end")
                    else:
                        entry_mru_v = float(self.entry_v.get().strip())
                        entry_mru_s0 = float(self.entry_s0.get().strip())
                        entry_mru_s = float(self.entry_sf.get().strip())
                        resultado = Mru().calcular_tempo(entry_mru_s,entry_mru_s0, entry_mru_v)
                        self._dialog_resposta_mru(resultado, "Tempo(t)",s0=entry_mru_s0, v=entry_mru_v, t=resultado)
                        self.entry_v.delete(0,"end")
                        self.entry_s0.delete(0,"end")
                        self.entry_sf.delete(0,"end")
                                                
                    
        except ValueError:
                self._dialog_erro("Insira valores válidos em todas as caixas de texto")
        
        
    def _dialog_resposta_mruv(self, resultados: list, reajustes: list, s0, s, v0, v, a, t, calculados):
        altura = 150 + len(resultados) * 30 + len(reajustes) * 25
        janela = self._top_level_settings("Resposta MRUV", f"420x{altura}", "assets/icon-ico/icon_certo_final.ico")
        ctk.CTkLabel(janela, text="Resultados possíveis:", 
                 text_color="yellow", font=("Arial", 14, "bold")).pack(pady=10)
        for l in resultados:
            ctk.CTkLabel(janela, text=l, text_color="green").pack(pady=4)
        if reajustes:
            ctk.CTkLabel(janela, text="Reajuste automático aplicado:", text_color="orange", font=("Arial", 11, "bold")).pack(pady=(12, 2))
            for reajuste in reajustes:
                ctk.CTkLabel(janela, text=reajuste, text_color="orange", font=("Arial", 10)).pack(pady=1)
        
        ctk.CTkButton(janela, text="Ver Gráficos", command= lambda: GraficoPage(self, "mruv",s0=s0, s=s, v0=v0, v=v, a=a, t=t, calculados=calculados)).pack(pady=20)
        janela.bind("<Return>", lambda event: GraficoPage(self, "mruv", s0=s0, s=s, v0=v0, v=v, a=a, t=t, calculados=calculados))
        janela.after(60_000, janela.destroy)

    def calcularMruv(self):
        def pegar(entry):
            val = entry.get().strip()
            return float(val) if val else None
        try:
        
            s0 = pegar(self.entry_s02)
            s  = pegar(self.entry_s2)
            v0 = pegar(self.entry_v0)
            v  = pegar(self.entry_vf)
            a  = pegar(self.entry_a)
            t  = pegar(self.entry_t2)
            
            ep = pegar(self.entry_ep) if self.checar_box_mruv1.get() else None
            self.entry_ep.delete(0,"end")
        except ValueError:
            self._dialog_erro("Houve um ERRO ao calcular o MRUV")
            return
    
        else:
            mruv = Mruv(s0=s0, s=s, v0=v0, v=v, a=a, t=t)

            tentativas_base = [("Posição Final (s)",          mruv.calcularPosicao),
            ("Velocidade Final (v)",       mruv.calcularVelocidadeFinal),
            ("Aceleração (pelo tempo)",    mruv.calcularAceleracaoPorTempo),
            ("Aceleração (Torricelli)",    mruv.calcularAceleracaoPorDistancia),
            ("Tempo (t)",                  mruv.calcularTempo),
            ("Vel. Inicial (pelo tempo)",  mruv.calcularVelocidadeInicialPeloTempo),
            ("Vel. Inicial (distância)",   mruv.calcularVelocidadeInicialPorDistancia),
            ("Espaço Percorrido (\u0394s)", mruv.calcularEspacoPercorrido)]

            resultados = []
            reajustes = []

            for nome, func in tentativas_base:
                try:
                    resultado = func()
                    resultados.append((nome, resultado))
                except (ValueError, TypeError, ZeroDivisionError):
                    pass
        
            if ep is not None:
                tentativas_ep = [
                    ("Aceleração (pelo espaço)", mruv.calcularAceleracaoPeloEspacoPercorrido),
                    ("Velocidade Final (pelo espaço)", mruv.calcularVelocidadeFinalPeloEspacoPercorrido),
                    ("Velocidade Inicial (pelo espaço)", mruv.calcularVelocidadeInicialPeloEspacoPercorrido),
                    ("Tempo (pelo espaço)", mruv.calcularTempoPeloEspacoPercorrido)
                ]
                for nome, func in tentativas_ep:
                    try:
                        resultados.append((nome, func(ep)))
                    except (ValueError, TypeError, ZeroDivisionError):
                        pass

            if not resultados:
                self._dialog_erro("Houve um ERRO ao calcular o MRUV")
                return 
            
            
            calculados = {nome: val for nome, val in resultados}

            if "Posição Final (s)" not in calculados and "Tempo (t)" in calculados:
                t_calc = calculados["Tempo (t)"]
                mruv_reaj = Mruv(s0=s0, s=s, v0=v0, v=v, a=a, t=t_calc)
                try: 
                    val = mruv_reaj.calcularPosicao()
                    resultados.append(("Posição Final (s): ", val))
                    calculados["Posição Final (s)"] = val
                    reajustes.append("Posição Final (s) <-- usou Tempo calculado")
                except (ValueError, TypeError, ZeroDivisionError):
                    pass

            for nome_a in ("Aceleração (pelo tempo)", "Aceleração (Torricelli)", "Aceleração (pelo espaço)"):
                if nome_a in calculados:
                    a_calc = calculados[nome_a]
                    mruv_reaj = Mruv(s0=s0, s=s, v0=v0, v=v, a=a_calc, t=t)
                    tentativas_reaj = [("Posição Final (s)",          mruv.calcularPosicao),
            ("Velocidade Final (v)",       mruv_reaj.calcularVelocidadeFinal),
            ("Aceleração (pelo tempo)",    mruv_reaj.calcularAceleracaoPorTempo),
            ("Aceleração (Torricelli)",    mruv_reaj.calcularAceleracaoPorDistancia),
            ("Tempo (t)",                  mruv_reaj.calcularTempo),
            ("Vel. Inicial (pelo tempo)",  mruv_reaj.calcularVelocidadeInicialPeloTempo),
            ("Vel. Inicial (distância)",   mruv_reaj.calcularVelocidadeInicialPorDistancia),
            ("Espaço Percorrido", mruv_reaj.calcularEspacoPercorrido)]
                    
                    for nome2, func2 in tentativas_reaj:
                        if nome2 not in calculados:
                            try:
                                val = func2()
                                resultados.append((nome2, val))
                                reajustes.append(f"{nome2}  <-- usou {nome_a} calculada")
                                calculados[nome2] = val
                            except (ValueError, TypeError, ZeroDivisionError, AttributeError):
                                pass
                    break

            linhas = [f"{nome}: {val:.2f}" for nome, val in resultados if val is not None]

            # Resolve valores finais para o gráfico, usando calculados como fallback
            a_final  = a  if a  is not None else (
                    calculados.get("Aceleração (pelo tempo)") or
                    calculados.get("Aceleração (Torricelli)") or
                    calculados.get("Aceleração (pelo espaço)"))

            t_final  = t  if t  is not None else (
                    calculados.get("Tempo (t)") or
                    calculados.get("Tempo (pelo espaço)"))

            v0_final = v0 if v0 is not None else (
                    calculados.get("Vel. Inicial (pelo tempo)") or
                    calculados.get("Vel. Inicial (distância)") or
                    calculados.get("Velocidade Inicial (pelo espaço)"))

            v_final  = v  if v  is not None else (
                    calculados.get("Velocidade Final (v)") or
                    calculados.get("Velocidade Final (pelo espaço)"))

            s0_final = s0 if s0 is not None else calculados.get("Posição Final (s)")

            self._dialog_resposta_mruv(
                linhas, reajustes,
                s0=s0_final, s=s,
                v0=v0_final, v=v_final,
                a=a_final,   t=t_final,
                calculados=calculados
            )
        finally:
            self.entry_s02.delete(0,"end")
            self.entry_s2.delete(0,"end")
            self.entry_v0.delete(0,"end")
            self.entry_vf.delete(0,"end")
            self.entry_a.delete(0,"end")
            self.entry_t2.delete(0,"end")
    # Utilitários
    
    def _top_level_settings(self, titulo: str, geometria: str, icon: str) -> ctk.CTkToplevel:
        janela = ctk.CTkToplevel(self)
        janela.geometry(geometria)
        janela.title(titulo)
        janela.after(250, lambda: janela.iconbitmap(icon))
        janela.attributes("-topmost", True)     # <-- fica sempre na frente
        janela.after(100, janela.lift)          # <-- aguarda renderizar
        janela.after(100, janela.focus_force)
        
        return janela