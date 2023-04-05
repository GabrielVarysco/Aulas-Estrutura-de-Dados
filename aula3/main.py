from Cidade import Cidade
from Pessoa import Pessoa
from Categoria import Categoria
from Produto import Produto
from Pedido import Pedido

poa = Cidade(1, "Porto Alegre")

p1 = Pessoa("João", "(51)123", poa)
p2 = Pessoa("Maria", "(51)234", poa)

#print(f"Nome da cidade da {p2.nome}: {p2.cidade.nome}")
#p1.imprimir()

print("--------- 29/03/2023 ----------")

cat1 = Categoria(1, "Bebida")
cat2 = Categoria(2, "Alimentos")

prod1 = Produto(1, "Coca-Cola", 5, cat1)
prod2 = Produto(2, "Pepsi", 4, cat1)
prod3 = Produto(3, "Arroz", 3.95, cat2)

ped1 = Pedido("Alberto Silva", p2)
ped1.addProduto(prod1)
ped1.addProduto(prod3)

ped1.imprimir()
