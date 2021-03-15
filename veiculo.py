
class Veiculo:

    def __init__(self, tipo, ano_fabricacao, modelo, cor):
        self.tipo = tipo
        self.ano_fabricacao = ano_fabricacao
        self.modelo = modelo
        self.cor = cor

    def setTipo(self, tipo):
        self.tipo = tipo

    def setAno_fabricacao(self, ano_fabricacao):
        self.ano_fabricacao = ano_fabricacao

    def setModelo(self, modelo):
        self.modelo = modelo

    def setCor(self, cor):
        self.cor = cor

    def getTipo(self):
        return self.tipo

    def getAno_fabricacao(self):
        return self.ano_fabricacao

    def getModelo(self):
        return self.modelo

    def getCor(self):
        return self.cor

