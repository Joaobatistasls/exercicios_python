# Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input("Me informe o 1° número: "))
b = int(input("Me informe o 2° número: "))
c = int(input("Me informe o 3° número: "))

if (a > b and a > c):
    maior = a
    print(maior)
elif (b > a and b > c):
    maior = b
    print(maior)
elif (c > a and c > b):
    maior = c
    print(maior)

if (a < b and a < c):
    menor = a
    print(menor)
elif (b < a and b < c):
    menor = b
    print(menor)
elif (c < a and c < b):
    menor = c 
    print(menor)

print("O número maior é {}".format(maior))
print("O número menor é {}".format(menor))