# Classe Pessoa: Crie uma classe que modele uma pessoa:
# a - Atributos: nome, idade e peso
# b -Métodos: Envelhercer e Classificação do peso.

# Criando a classe pessoa 
class Pessoa:
    # Criando os atributos
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
    
    # Criando o método para verificar a faixa de idade
    def envelhecer(self):
        if (self.idade <= 12):
            print(f"Sua idade é {self.idade} e você é uma Criança..")
        elif (self.idade < 18):
            print("Sua idade é {} e você é um Adolescente..".format(self.idade))
        elif (self.idade >= 18):
            print(f"Sua idade é {self.idade} e você é um Adulto..")
        elif (self.idade >= 60):
            print("Sua iddade é {} e você é um adulto..".format(self.idade))

    # Criando o método para verificar se está no peso normal
    def faixa_peso(self):
        if (self.peso >= 18.50 and self.peso <= 24.99):
            print("Seu peso é Normal..")
        elif (self.peso >= 25.00 and self.peso <= 29.99):
            print("Seu peso é Pré - Obesidade..")
        elif (self.peso >= 30.00 and self.peso <= 34.90):
            print("Seu peso é Pré - Obesidade Grau I..")
        elif (self.peso >= 35.00 and self.peso <= 39.99):
            print("Seu peso é Pré - Obesidade Grau II..")

pessoa = Pessoa("João", 19)

print(pessoa.envelhecer())
        