# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas letras do alfabeto foram lidas. Imprima as letras do alfabeto.

lista = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5]

lista_com_alfabeto = []
lista_com_numeros = []

for elementos in lista:
    if(type(elementos) == str):
        lista_com_alfabeto.append(elementos)
        qt_letras = len(lista_com_alfabeto)
    else:
        lista_com_numeros.append(elementos)
        qt_numeros = len(lista_com_numeros)

print(f"Lista do alfabeto: {lista_com_alfabeto} e a quantidade é {qt_letras}")
print(f"Lista do numero : {lista_com_numeros} e a quantidade é {qt_numeros}")



