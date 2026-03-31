class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def adicionar(self, valor):
        self.quantidade += valor

    def remover(self, valor):
        self.quantidade -= valor

    def mostrar_dados(self):
        print(f"Produto: {self.nome} / Quantidade: {self.quantidade}") 

class ProdutoPerecivel(Produto):
    def mostrar_dados(self):
        print(f"{self.nome} (Perecível) - {self.quantidade}")

class ProdutoDigital(Produto):
    def mostrar_dados(self):
        print(f"{self.nome} (Digital) - {self.quantidade}")