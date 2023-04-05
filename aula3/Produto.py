#from Categoria import Categoria
#tentar fazer com import em casa

class Produto:
    def __init__(self, id, name, preco, categoria):
        self.id = id
        self.name = name
        self.preco = preco
        self.cat = categoria
    
    def imprimir(self):
        print(f"""Nome: {self.name}
                Preço: {self.preco}
                Categoria: {self.cat.name}""")
