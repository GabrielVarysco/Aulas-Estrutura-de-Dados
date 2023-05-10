from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id = 0, nome = None, telefone = None):
        self.id = id
        self.nome= nome
        self._telefone = telefone

    @abstractmethod
    def marcarPresenca(self):
        pass

    def matricular():
        pass

    def imprimir(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self._telefone}")
        
    @abstractmethod
    def imprimirEspecifico(self):
        pass