# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = []
multiplicar = 1

for numeros in range(1, 6):
    num = int(input("Digite p {]° número: }".format(numeros)))
    lista.append(num)

    multiplicar = multiplicar * num

    somar = sum(lista)

print("A lista com os números são: {}, com a multiplicação o valor é: {} e com a somar é {}".format(lista, multiplicar, somar))

