class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print(f"ID: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")