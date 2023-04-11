# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

# Variávies 
todos_os_numeros = []
numeros_par = []
numeros_impar = []

# for para fazer interação até o número 20
for numeros in range(1, 21):
    # Método para exibir todos os números
    todos_os_numeros.append(numeros)

    # verificanção para sabe se o número é par ou ímpar
    if (numeros % 2 == 0):
        numeros_par.append(numeros)
    else:
        numeros_impar.append(numeros)

# mensagens para exibir os números 
print(f"Todos os números: {todos_os_numeros}")
print(f"Números pares: {numeros_par}")
print(f"Números ímpar: {numeros_impar}")


