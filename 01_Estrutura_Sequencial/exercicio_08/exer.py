# Faça um Programa que pergunte 
# Quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

ganha_por_hora = float(input("Quanto você ganha por hora? "))
quantas_hora_mes = int(input("Quantas hora você trabalha por mês? "))

salario = int(ganha_por_hora * quantas_hora_mes)

print(f"Seu salário é {salario}. Estude mais pra ganhar mais!!")