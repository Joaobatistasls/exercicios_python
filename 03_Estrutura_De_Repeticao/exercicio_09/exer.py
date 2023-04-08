# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

numeros = 50

for number in range(1, numeros + 1):
    if (number % 2 == 1):
        print("O número {} é ímpar!".format(number))
    
    