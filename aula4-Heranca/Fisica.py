from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, nome, fone, cidade, cpf):
        super().__init__( nome, fone, cidade) #chama os parametros que serão herdados da outra classe
        self.cpf = cpf
        self.empresa = None
    
    def setEmpresa(self, empresa):
        self.empresa = empresa