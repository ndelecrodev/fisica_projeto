class Mru:

    def calcularPosicaoFinal(self,t: float, s0:float, v: float) -> float:
        return s0 + v * t
    
    def calcular_tempo(self, s: float, s0:float, v:float):
        return ((s - s0) / v)
    
    def calcular_tempo_espaco(self, espaco: float, v:float):
        return (espaco / v)
    
    def calcular_velocidade_espaco(self, espaco:float, t:float):
        return espaco / t
    
    def calcular_velocidade(self, s0:float, t:float, s:float):
        return (s - s0) / t