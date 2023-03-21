# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
# O rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
# Que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
# Pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um
# Programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o 
# Valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


peso = int(input("Digite o peso do peixe: "))
multa = 4.00
limite = 50 

if (peso > limite): 
    print(f"Seu peso é: {peso}")
    print(f"Seu peso passsou o limite!! Sua multa é de: {multa} por quilo excendente")
else:
    print(f"Seu peso é: {peso}")
    print("Você não passou do limite!")