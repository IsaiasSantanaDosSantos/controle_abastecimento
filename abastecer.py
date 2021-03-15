from veiculo import Veiculo

class Abastecer:
    def __init__(self,qtde_comb, km_abast, tipo, ano_fabricacao, modelo, cor):
        super().__init__(tipo, ano_fabricacao, modelo, cor)
        self.qtde_comb = qtde_comb
        self.km_abast = km_abast

    def setQtde_comb(self, qtde_comb):
        self.qtde_comb = qtde_comb

    def setKm_abast(self, km_abast):
        self.km_abast = km_abast

    def getQtde_comb(self):
        return self.qtde_comb

    def getKm_abast(self):
        return self.km_abast

