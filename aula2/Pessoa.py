class Pessoa:

    idade = None

    def __init__(self, nome, idade):
        print("Objseto instanciado!")
        self.nome = nome
        self.idade = idade
        self.fone = input("Digite seu fone:")

    def imprimir(self):
        print(f"Nome: {self.nome}\n"
              f"Idade: {self.idade}\n"
              f"Telefone: {self.fone}")
