from models.produtos import Produto
from services.estoque import Estoque

estoque = Estoque()

p1 = Produto("Mouse", 10)
p2 = Produto("Teclado", 5)

estoque.adicionar_produto(p1)
estoque.adicionar_produto(p2)

produto_encontrado = estoque.buscar_produto("Mouse")

if produto_encontrado:
    print("Produto encontrado:", produto_encontrado.nome, produto_encontrado.quantidade)
else:
    print("Produto não encontrado")