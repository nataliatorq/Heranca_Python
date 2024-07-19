from superclasse import Veiculo


# Classe de Teste
class Carro(Veiculo):
    def _init_(self, marca, modelo, ano, cor):
        super()._init_(marca, modelo, ano, cor),

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, novo_modelo):
        self._modelo = novo_modelo


meu_carro = Carro("Toyota", "Corolla", 2020, "Prata")

print("Marca:", meu_carro.marca)
print("Cor:", meu_carro.cor)

print("Modelo:", meu_carro.get_modelo())

print("Ano:", meu_carro.get_ano())

meu_carro.set_modelo("Camry")
meu_carro.set_ano(2022)

print("\nApós modificação:")
print("Modelo:", meu_carro.get_modelo())
print("Ano:", meu_carro.get_ano())