from models.produtos import Produto
class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade):
        produto = Produto(nome, quantidade)
        self.produtos.append(produto)
        return "Produto adicionado com sucesso"
    
    def listar_produto(self):
        return [p.to_dict() for p in self.produtos]
    
    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto.to_dict()
        return "Produto não encontrado"

    def atualizar_quantidade(self, nome, nova_quantidade):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                produto.quantidade = nova_quantidade
                return "Quantidade atualizada"
        return "Produto não encontrado"
    
    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                self.produtos.remove(produto)
                return "Produto removido"
        return "Produto não encontrado"

estoque = Estoque()

## GET = listar
## POST = criar
## PUT = atualizar
## DELETE = remover

## Simulação dessas rotas de uma API 

def get_produtos():
    return estoque.listar_produto()

def post_produto(nome, quantidade):
    return estoque.adicionar_produto(nome, quantidade)

def get_produto_por_nome(nome):
    return estoque.buscar_produto(nome)

def put_produto(nome, quantidade):
    return estoque.atualizar_quantidade(nome, quantidade)

def delete_produto(nome):
    return estoque.remover_produto(nome)





def executar_rota(rota, metodo, dados=None):
    if rota == "/produtos" and metodo == "GET":
        return get_produtos()
    
    if rota == "/produtos" and metodo == "POST":
        return post_produto(dados["nome"], dados["quantidade"])
    
    if rota == "/produtos/buscar" and metodo == "GET":
        return get_produto_por_nome(dados["nome"])
    
    if rota == "/produtos/atualizar" and metodo == "PUT":
        return put_produto(dados["nome"], dados["quantidade"])
    
    if rota == "/produtos/deletar" and metodo == "DELETE":
        return delete_produto(dados["nome"])
    
    return "Rota não encontrada - ERRO"