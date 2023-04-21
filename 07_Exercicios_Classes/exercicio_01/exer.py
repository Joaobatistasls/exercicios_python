# Classe Bola: Crie uma classe que modele uma bola:
# a - Atributos: Cor, circunferência, material
# b - Métodos: trocaCor e mostraCor


# Criando a classe Bola
class Bola:
    # Criando a função contrutora e passando os parâmetros para os atributos
    def _init_(self, cor, circuferencia, material):
        # Criando os atributos
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = [material]
        
    # Método para trocar a cor da bola
    def trocar_cor(self, cor):
        self.cor = cor
        print("A cor foi alterada para {}".format(self.cor))
        
    # Método para mostrar a cor
    def mostra_cor(self):
        print("A cor é {}".format(self.cor))
      
# Criando uma referência  
bola = Bola("Roxo", 69.5, ["borachar", "Couro"])


# Imprimindo e chamando o método para trocar a cor
print(bola.trocar_cor("Laranja"))

print(bola.mostra_cor())