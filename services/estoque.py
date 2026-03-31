class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for p in self.produtos:
            p.mostrar_dados()

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto
        return None

    def atualizar_quantidade(self, nome, nova_quantidade):
        produto = self.buscar_produto(nome)
        if produto is not None:
            produto.quantidade = nova_quantidade
            return True
        return False