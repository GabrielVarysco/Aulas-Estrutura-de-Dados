from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo = None, cor = None, preco = 0, potencialDaFonte = 0):
        super().__init__(modelo, cor, preco)
        self._potencialDaFonte = potencialDaFonte
    
    def getInformacoes(self):
        return super().getInformacoes(), self._potencialDaFonte

    def imprimir(self):
        print("Desktop: ")
        super().imprimir()
    
    def cadastrar(self):
        super().imprimir()
        print(f"Potencial da fonte: {str(self._potencialDaFonte)}W")