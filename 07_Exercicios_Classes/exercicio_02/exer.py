# Classe Quadrado: Crie uma classe que modele um quadrado:
# a - Atributos: Tamanho do lado
# b - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

# Criando a classe Quandrado
class Quadrado:
    def _init_(self, tamanho):
        self.__tamanho = tamanho

    # Mudar lado
    def mudar_lado(self, tamanho):
        self.__tamanho = tamanho
        print("O tamanho do quadrado foi alterado para {}".format(self.__tamanho))
    
    # Retorna lado do quadrado
    def retorna_lado(self):
        print(f"O valor do lado é {self.__tamanho}")
    
# Criando referência
quadrado = Quadrado(15)

# Imprimindo o método
print(quadrado.retorna_lado())