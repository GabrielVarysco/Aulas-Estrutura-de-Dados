from Veiculo import Veiculo
    
class Drone(Veiculo):
    def __init__(self, modelo=None, marca=None, qtdHelices=4):
        super().__init__(modelo, marca)
        self._qtdHelices = qtdHelices
    
    def imprimirEspecifico(self):
        super().imprimir()
        print(f"Portas: {str(self._qtdPortas)}")