from Aluno import Aluno

class AluGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print(f"ID: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")
        print(f"Semestre: {self.semestre}")