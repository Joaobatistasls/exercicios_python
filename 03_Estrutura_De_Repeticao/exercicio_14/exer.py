# Faça um programa que peça 10 números inteiros, calcule e 
# Mostre a quantidade de números pares e a quantidade de números impares.

numeros_inteiros = 10
lista_par = []
lista_impar = []

for numeros in range(1, numeros_inteiros + 1):
    if (numeros % 2 == 0):
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)

print(len(lista_par))
print(len(lista_impar))


# Forma que o victor ensinou
lista_par, lista_impar = [], []

for numeros in range(11):
    lista_par.append(numeros) if (numeros % 2 == 0) else lista_impar.append(numeros)

print(lista_par, lista_impar)