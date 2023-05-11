from abc import ABC, abstractmethod


class Computador(ABC):
    def __init__(self, modelo = None, cor = None, preco = 0):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        return self.modelo, self.cor, self.preco
    
    def imprimir(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Preço: {self.preco}")
        
    @abstractmethod
    def cadastrar(self):
        pass