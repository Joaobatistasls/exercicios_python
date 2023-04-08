# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

numeros = 20 

for number in range(1, numeros + 1):
    print(number)

    if (number == 20):
        print(list(range(1, numeros + 1)))

        