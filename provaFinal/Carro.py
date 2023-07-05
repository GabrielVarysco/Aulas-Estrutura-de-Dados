from Veiculo import Veiculo
    
class Carro(Veiculo):
    def __init__(self, modelo=None, marca=None, portas = 4):
        super().__init__(modelo, marca)
        self.__portas = portas
    
    def imprimirEspecifico(self):
        super().imprimir()
        print(f"Portas: {str(self.__portas)}")