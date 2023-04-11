# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 
# 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista_um = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_dois = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista_tres = []

for numeros in lista_um:
    lista_tres.append(numeros)

for numeros in lista_dois:
    lista_tres.append(numeros)

print("Os números do terceiro vetor é: {}".format(lista_tres))


