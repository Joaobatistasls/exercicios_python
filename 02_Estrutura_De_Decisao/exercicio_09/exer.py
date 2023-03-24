# Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = int(input("Escreva um número: "))
b = int(input("Escreva um número: "))
c = int(input("Escreva um número: "))

if (a < c):
    a, c = c, a
elif (a < b):
    a, b = b, a
elif (b < c):
    b, c = c, b

print(f"A ordem descrescente é {a}, {b} e {c}")

