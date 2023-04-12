# Faça um programa para imprimir:
# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def imprimir_numeros(n):
    for numero in range(1, n + 1):
        for linha in range(1, numero + 1):
            print(linha, end=" ")
        print()

n = int(input("Digite um número inteiro: "))
imprimir_numeros