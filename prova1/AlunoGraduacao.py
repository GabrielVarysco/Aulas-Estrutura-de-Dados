from Pessoa import Pessoa

class AlunoGraduacao(Pessoa):
    def __init__(self, id = 0, nome = None, matricula = None, presenca = 0):
        super().__init__(id, nome)
        self.__matricula = matricula
        self.presenca = presenca

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self):
        self.__matricula = input("Digite a matricula: ")

    def marcarPresenca(self):
        return super().marcarPresenca(), self.presenca

    def imprimirEspecifico(self):
        super().imprimir()
        print(f"Matricula: {self.__matricula}")
        print(f"Presenca: {str(self.presenca)}")