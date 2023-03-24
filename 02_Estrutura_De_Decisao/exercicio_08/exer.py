# Faça um programa que pergunte o preço de três produtos
# E informe qual produto você deve comprar, 
# Sabendo que a decisão é sempre pelo mais barato.

a = float(input("Qual o preço do 1° produto: "))
b = float(input("Qual o preço do 2° produto: "))
c = float(input("Qual o preço do 3° produto: "))

if (a < b and a < c):
    barato = a
    print(f"O produto mais barato é: {barato}")
elif (b < a and b < c):
    barato = b 
    print(f"O produto mais barato é: {barato}")
elif (c < a and c < b):
    barato = c
    print(f"O produto mais barato é: {barato}")