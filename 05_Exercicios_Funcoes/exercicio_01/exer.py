# Faça um programa para imprimir:
#  1
#  2   2
#  3   3   3
#  .....
#  n   n   n   n   n   n  ... n
# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimir(numero):
  print(f"{str(numero)} " * numero)

numero = int(input("Digite um número: "))

for num in range(1, numero + 1):
  imprimir(num)