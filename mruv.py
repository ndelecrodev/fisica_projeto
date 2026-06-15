import math

# Classe que representa o Movimento Retilíneo Uniformemente Variado (MRUV)
class Mruv:
    # Construtor da classe
    # Recebe todas as variáveis principais do MRUV
    def __init__(self, s0 = None, s = None, v0 = None, v = None, a = None, t = None):
        self.s0 = s0  # posição inicial
        self.s = s    # posição final
        self.v0 = v0  # velocidade inicial
        self.v = v    # velocidade final
        self.a = a    # aceleração
        self.t = t    # tempo
        
    # POSIÇÃO FINAL
    # Fórmula: s = s0 + v0.t + (a.t²)/2
    def calcularPosicao(self):

        # Verifica se todos os dados necessários foram informados
        if None in (self.s0, self.v0, self.a, self.t):
            raise ValueError("Necessário: s0, v0, a, t")

        # Retorna o cálculo da posição final
        return self.s0 + self.v0 * self.t + (self.a * self.t**2) / 2


    # VELOCIDADE FINAL
    # Fórmula: v = v0 + a.t

    def calcularVelocidadeFinal(self):

        # Confere se os valores necessários existem
        if None in (self.v0, self.a, self.t):
            raise ValueError("Necessário: v0, a, t")

        # Retorna a velocidade final
        return self.v0 + self.a * self.t


    # ACELERAÇÃO
        # Calcula aceleração usando tempo
        # Fórmula: a = (v - v0)/t
    def calcularAceleracaoPorTempo(self):

        # Verifica se os valores foram preenchidos
        if None in (self.v, self.v0, self.t):
            raise ValueError("Necessário: v, v0, t")

        # Evita divisão por zero
        if self.t == 0:
            raise ValueError("Tempo não pode ser zero")

        # Retorna a aceleração
        return (self.v - self.v0) / self.t

        # Calcula aceleração usando distância (Equação de Torricelli)
        # Fórmula: a = (v² - v0²)/(2.Δs)
    
    def calcularAceleracaoPorDistancia(self):

        # Verifica os dados necessários
        if None in (self.v, self.v0, self.s, self.s0):
            raise ValueError("Necessário: v, v0, s, s0")

        # Calcula o deslocamento
        delta_s = self.s - self.s0

        # Evita divisão por zero
        if delta_s == 0:
            raise ValueError("Distância não pode ser zero")

        # Retorna a aceleração
        return (self.v**2 - self.v0**2) / (2 * delta_s)

    # TEMPO
    # Fórmula: t = (v - v0)/a
    def calcularTempo(self):

        # Verifica se os dados existem
        if None in (self.v, self.v0, self.a):
            raise ValueError("Necessário: v, v0, a")

        # Evita divisão por zero
        if self.a == 0:
            raise ValueError("Aceleração não pode ser zero")

        # Retorna o tempo
        return (self.v - self.v0) / self.a
    
    # VELOCIDADE INICIAL

        # Calcula velocidade inicial usando tempo
        # Fórmula: v0 = v - a.t
    def calcularVelocidadeInicialPeloTempo(self):

        # Verifica os dados necessários
        if None in (self.v, self.a, self.t):
            raise ValueError("Necessário: v, a, t")

        # Retorna a velocidade inicial
        return self.v - self.a * self.t
    
        # Calcula velocidade inicial usando distância
        # Fórmula derivada de Torricelli
   
    def calcularVelocidadeInicialPorDistancia(self):

        # Verifica os dados necessários
        if None in (self.v, self.a, self.s, self.s0):
            raise ValueError("Necessário: v, a, s, s0")

        # Calcula deslocamento
        delta_s = self.s - self.s0

        # Parte interna da raiz quadrada
        valor = self.v**2 - 2 * self.a * delta_s

        # Evita raiz quadrada negativa
        if valor < 0:
            raise ValueError("Resultado inválido: raiz de número negativo")

        # math.sqrt() calcula raiz quadrada
        return math.sqrt(valor)
    
    def calcularEspacoPercorrido(self):
        if None not in (self.v0, self.a, self.t):
            return (self.v0*self.t) + ((self.a*self.t**2)/2)
        if None not in (self.v, self.v0, self.a):
            if self.a == 0:
                raise ValueError("Aceleração não pode ser zero")
            return (self.v**2 - self.v0**2) / (2*self.a)
        if None not in (self.v0, self.v, self.t):
            return ((self.v0 + self.v) / 2)*self.t
        
        raise ValueError("Não foi possivel calcular o espaço percorrido")

    def calcularAceleracaoPeloEspacoPercorrido(self, espaco_percorrido: float):
        if None not in (self.v, self.v0):
            return (self.v**2 - self.v0**2) / (2*espaco_percorrido)
        if None not in (self.v0, self.t):
            return (2*(espaco_percorrido - self.v0 * self.t)) / self.t**2
        
        raise ValueError("Não foi possivel calcular a Aceleração por meio do espaço percorrido")
        
    def calcularVelocidadeFinalPeloEspacoPercorrido(self, espaco_percorrido: float):
        if None not in (self.v0, self.a):
            valor = self.v0**2 + 2 * self.a * espaco_percorrido
            if valor < 0:
                raise ValueError("Raiz Negativa")
            return math.sqrt(valor)

        raise ValueError("Não foi possivel calcular a Velocidade Final por meio do espaço percorrido")

    def calcularVelocidadeInicialPeloEspacoPercorrido(self, espaco_percorrido: float):
        if None not in (self.v, self.a):
            valor = self.v**2 - 2 * self.a * espaco_percorrido
            if valor < 0:
                raise ValueError("Raiz Negativa")
            return math.sqrt(valor)        
        raise ValueError("Não foi possivel calcular a Velocidade Inicial por meio do espaço percorrido")

    def calcular_tempo_mruv_espaco(delta_s, v0, a):
            # 1. Validação de segurança: se a aceleração for zero, não é MRUV!
            if a == 0:
                if v0 == 0:
                    raise ValueError("O objeto está parado (v0 e aceleração são zero).")
                # Se a = 0 mas tem velocidade, cai na regra do MRU simples
                t = delta_s / v0
                if t < 0:
                    raise ValueError("Tempo negativo (movimento impossível).")
                return t 
            # 2. Definindo os coeficientes de Bhaskara
            A = a / 2
            B = v0
            C = -delta_s  # Lembra que o Delta S passa subtraindo

            # 3. Calculando o Delta (b² - 4ac)
            delta = (B ** 2) - (4 * A * C)

            # 4. Validação do Delta: se for negativo, não há raiz real
            if delta < 0:
                raise ValueError("Erro: O objeto nunca alcançará essa distância nessas condições.")

            # 5. Calculando as duas raízes de Bhaskara (t1 e t2)
            raiz_delta = math.sqrt(delta)
            t1 = (-B + raiz_delta) / (2 * A)
            t2 = (-B - raiz_delta) / (2 * A)

            # 6. Filtrando o tempo correto (o tempo físico deve ser positivo)
            tempos_validos = [t for t in (t1, t2) if t >= 0]
            

            if not tempos_validos:
                raise ValueError("Erro: Os tempos calculados são negativos (movimento impossível).")
            
            return min(tempos_validos)

    def calcularTempoPeloEspacoPercorrido(self, espaco_percorrido: float):
        
        if None not in (self.v0, self.v):
            if (self.v0 + self.v) == 0:
                raise ValueError("Soma das velocidades não pode ser zero")
            return(2*espaco_percorrido) / (self.v0 + self.v)        
        
        if None not in (self.a, self.v0):
            return self.calcular_tempo_mruv_espaco(espaco_percorrido, self.v0, self.a)
        raise ValueError("Dados Insuficientes")