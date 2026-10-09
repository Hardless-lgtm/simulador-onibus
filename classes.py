class Rua:
    def __init__(self, nome: str, comprimento: float, velocidade_maxima: float):
        self.nome = nome
        self.comprimento = comprimento  # metros
        self.velocidade_maxima = velocidade_maxima  # km/h


class PontoOnibus:
    def __init__(self, nome: str, rua: Rua, posicao: int, tempo_parada: float):
        self.nome = nome
        self.rua = rua  # Objeto Rua
        self.posicao = posicao  # metros desde o início da rua
        self.tempo_parada = tempo_parada  # segundos


class Linha:
    def __init__(self, nome: str):
        self.nome = nome
        self.ruas = []
        self.pontos = []

    def adicionar_rua(self, rua: Rua):
        self.ruas.append(rua)

    def adicionar_ponto(self, ponto):
        self.pontos.append(ponto)


class Onibus:
    def __init__(self, identificacao: int, linha: Linha):
        self.identificacao = identificacao
        self.linha = linha  # Objeto Linha

        self.rua_atual = None
        self.posicao = 0  # metros desde o início da rua atual
        self.velocidade_atual = 0  # km/h
        self.atraso = 0  # segundos
        self.estado = "parado"


class Simulador:
    def __init__(self):
        self.onibus = []
        self.tempo_simulado = 0  # segundos

    def adicionar_onibus(self, onibus):
        self.onibus.append(onibus)