# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# a - Idade: entre 0 e 150;
# b - Salário: maior que zero;
# c - Sexo: 'f' ou 'm';

inicio = 1
tentativas = 100

while (inicio <= tentativas):
    qt_nome = input("Me informe seu nome: ")
    nome = len(qt_nome)
    idade = int(input("Me informe a sua idade: "))
    salario = float(input("Me informe seu salário: "))
    sexo = input("Me informe o seu gênero: ")

    if (nome < 3):
        print("Seu nome deve ter no mínimo 3 caracteres!")
        continue

    if (idade < 0 or idade > 150):
        print("Sua idade dever está entre 0 e 150!")
        continue
    
    if (salario < 0):
        print("Seu salário dever ser maior que 0!")
        continue

    if (sexo == "f" or sexo == "feminino"):
        print("seu sexo é [F] - Feminino!")
    elif (sexo == "m" or sexo == "masculino"):
        print("Seu sexo é [M] - Masculino")
    else:
        continue

    break