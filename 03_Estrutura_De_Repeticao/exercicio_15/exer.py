# Faça um programa que calcule o fatorial de um número inteiro 
# Fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Fatorial de: "))

resultado = 1

for n in range(1, numero + 1):
    resultado = resultado * n

print(resultado)
