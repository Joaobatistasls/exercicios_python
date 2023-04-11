# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada 
# Informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

lista_idade = []
lista_altura = []

for infor in range(1, 6):
    idade = int(input("Informe sua idade {}° pessoa: ".format(infor)))
    altura = int(input("Informe sau altura {}° pessoa: ".format(infor)))

    lista_idade.append(idade)
    lista_altura.append(altura)

print("As idades são: {}".format(lista_idade))
print("AS alturas são: {}".format(lista_altura))

