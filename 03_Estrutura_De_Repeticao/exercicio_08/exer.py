# Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = 5

for number in range(1, numeros + 1):
    print(number)
    
    somar = number + number
    media = number / 2

    print("A somar do número é: {}".format(somar))
    print("A média do número é: {}".format(media))

