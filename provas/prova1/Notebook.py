from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo = None, cor = None, preco = 0, tempoDeBateria = 0):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
    
    def getInformacoes(self):
        return super().getInformacoes(), self.__tempoDeBateria

    def imprimir(self):
        print("Notebook: ")
        super().imprimir()
    
    def cadastrar(self):
        super().imprimir()
        print(f"Tempo de bateria: {str(self.__tempoDeBateria)}h")