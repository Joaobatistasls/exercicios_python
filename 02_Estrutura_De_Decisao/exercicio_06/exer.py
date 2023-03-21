# Faça um Programa que leia três números e mostre o maior deles.

numero_um = int(input("Me informe o 1° número: "))
numero_dois = int(input("Me informe o 2° número: "))
numero_tres = int(input("Me informe o 3° número: "))

if (numero_um > numero_dois and numero_um > numero_tres):
    print(numero_um)
elif (numero_dois > numero_um and numero_dois > numero_tres):
    print(numero_dois)
elif (numero_tres > numero_um and numero_tres > numero_dois):
    print(numero_tres)

