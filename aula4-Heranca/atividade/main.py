from Aluno import Aluno
from AluEnsMedio import AluEnsMedio
from AluGraduacao import AluGraduacao

a1 = Aluno(1, "Gabriel", 123)
a2 = Aluno(2, "Maria", 456)

aEM1 = AluEnsMedio(1, "Gabriel", 123, 8)
aEM2 = AluEnsMedio(2, "Maria", 456, 9)

aG1 = AluGraduacao(1, "Gabriel", 123, 3)
aG2 = AluGraduacao(2, "Maria", 456, 2)

aG1.imprimir()