# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num 
# Vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

total = 10
alunos = 1
lista_notas = []

while (alunos <= total):
    print(f"Aluno {alunos} Informe suas 4 notas.")
    
    for nota in range(1, 5):
        notas = float(input(f"Informe sua {nota}° nota: "))

    media = (notas + notas + notas + notas) / 4 
    lista_notas.append(media)
    print(lista_notas)

    alunos_aprovados = 0
    if (media >= 7.0):
        alunos_aprovados = alunos_aprovados + 1

    alunos = alunos + 1

print(f"O total de alunos aprovados com a média maior ou igual a 7.0 é: {alunos_aprovados}")

