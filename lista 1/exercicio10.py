class Veiculo:
    def tipo_habilitacao(self):
        pass

class Carro(Veiculo):
    def tipo_habilitacao(self):
        return "Categoria B"

class Moto(Veiculo):
    def tipo_habilitacao(self):
        return "Categoria A"

frota = [Carro(), Moto()]
for v in frota:
    print(f"Habilitação necessária: {v.tipo_habilitacao()}")