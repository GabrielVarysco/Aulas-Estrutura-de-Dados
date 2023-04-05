from Pessoa import Pessoa
from Fisica import Fisica

class Juridica(Pessoa):
    def __init__(self, nome, fone, cidade, cnpj):
        super().__init__(nome, fone, cidade)
        self.cnpj = cnpj
        self.qtd_funcionarios = 0
        self.funcionarios = []

    def addFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
        self.qtd_funcionarios += 1
    
    def imprimir(self):
        print("---------------------------------------------")
        print(f"Empresa: {self.nome}")
        print(f"Fone: {self.fone}")
        print(f"Cidade: {self.cidade.nome}")
        print(f"Quantidade de funcionarios: {self.qtd_funcionarios}")
        print(f"Funcionários:")
        if len(self.funcionarios) > 0:
            for func in self.funcionarios:
                print(f"Nome: {func.nome}")
                print(f"Fone: {func.fone}")
                print(f"Cidade: {func.cidade.nome}")
        else:
            print("Nenhum funcionário registrado.")
        print("---------------------------------------------")
