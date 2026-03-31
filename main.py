from models.produtos import Produto
from models.produtos import ProdutoPerecivel
from models.produtos import ProdutoDigital
from services.estoque import Estoque

estoque = Estoque()

produto1 = Produto("Mouse", 10)
produto2 = ProdutoPerecivel("Batata", 5)
produto3 = ProdutoDigital("Ebook", 8)

estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
estoque.adicionar_produto(produto3)

estoque.listar_produtos()

