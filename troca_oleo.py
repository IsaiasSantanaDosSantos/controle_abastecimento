from veiculo import Veiculo

class TrocaOleo:

    def __init__(self, kms, tipo, ano_fabricacao, modelo, cor):
        super().__init__(kms, tipo, ano_fabricacao, modelo, cor)
        self.kms = kms

    def setKms(self, kms):
        self.kms = kms

    def getKms(self):
        return self.kms
