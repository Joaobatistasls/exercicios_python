# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
# O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.

# Criando o objeto
class Tv:

    # Criando o Construtor
    def __init__(self, canal, volume):
        # Criando os atributos
        self.canal = canal
        self.volume = volume
    
    # Criando método Informar o canal da tv
    def canal_tv(self):
        if (self.canal <= 50):
            print(f"O canal da tv é o {self.canal} e o volume está {self.volume}%")
        else:
            print("Só temos 50 canais disponíveis..")

    # Criando o método para volume
    def volume_tv(self, volume):
        self.volume = volume
        if (self.volume >= 50 and self.volume <= 100):
            print(f"O volume está aumentando e esta em {self.volume}%")
        elif (self.volume > 100):
            print("O volume tem que ser abaixo de 100%")
        elif (self.volume < 50):
            print(f"O volume está baixo e está em {self.volume}%")

# Criando a referência
televisao = Tv(12, 70)

# Imprimindo o método
print(televisao.volume_tv(120))