from Cidade import Cidade
from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

c1 = Cidade(1, "Porto Alegre")
c2 = Cidade(2, "Capão da Canoa")

joao = Fisica("João", "9111-11111", c1, "000.111.222-33")
maria = Fisica("Maria", "9222-22222", c2, "222.222.333-44")
jose = Fisica("José", "9222-22222", c2, "333.333.444-55")

dosul = Juridica("Supermercado Dosul", "1234-4567", c1, "01.234.567/0001-00")

dosul.addFuncionario(joao)
dosul.addFuncionario(maria)

dosul.imprimir()
