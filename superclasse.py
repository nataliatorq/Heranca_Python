class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca              
        self._modelo = modelo           
        self.__ano = ano                
        self.cor = cor

    def get_ano(self):
        return self.__ano

    def set_ano(self, novo_ano):
        self.__ano = novo_ano