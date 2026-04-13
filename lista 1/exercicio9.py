class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
        else:
            print("Estoque insuficiente!")

    def repor(self, quantidade):
        self.estoque += quantidade

    def exibir_info(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque}")

# Teste
p = Produto("Mouse", 50.0, 10)
p.vender(3)
p.exibir_info()