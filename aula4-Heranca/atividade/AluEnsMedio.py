from Aluno import Aluno

class AluEnsMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self.ano = ano
    
    def imprimir(self):
        print(f"ID: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")
        print(f"Ano: {self.ano}")