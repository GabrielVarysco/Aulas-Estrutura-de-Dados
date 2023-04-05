from Cidade import Cidade

class Pessoa:
    def __init__(self, name = None, fone = None, city = Cidade(None ,None)):
        self.id = None
        self.nome = name
        self.fone = fone
        self.cidade = city
    
    def imprimir(self):
        print(f"Nome {self.nome}")
        print(f"Telefone: {self.fone}")
        print(f"Cidade: {self.cidade}")
    