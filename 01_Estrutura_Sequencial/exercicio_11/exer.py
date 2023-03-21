# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que 
# Calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = int(input("Qual a sua altura? "))

peso_ideal = (72.7 * altura) / 58 

peso = int(peso_ideal)

print(f"O pesso ideal é: {peso}")

