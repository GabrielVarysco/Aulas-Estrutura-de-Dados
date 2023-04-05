#from Categoria import Categoria
#from Produto import Produto
#tentar fazer com import em casa

class Pedido:
    def __init__(self, endereco, cliente):
        self.id = None
        self.end = endereco
        self.cliente = cliente
        self.produtos = []
    
    def addProduto(self, produto):
        self.produtos.append(produto)
        soma = 0

        for prod in self.produtos:
            soma += prod.preco
        return soma

    def imprimir(self):
        print(f"Cliente: {self.cliente.nome}")
        print(f"Endereço: {self.end}")
        print(f"Cidade: {self.cliente.cidade.nome}")
        print(f"--------- Produtos ---------")
        if len(self.produtos) == 0:
            print("Pedido vazio!")
        else:
            soma = 0
            for prod in self.produtos:
                soma += prod.preco
                print(f"Produto: {prod.name}")
                print(f"Preço: {prod.preco}")
                print(f"Categoria: {prod.cat.name}")
            print(f"Total: {soma}")
            print("------------------------")
