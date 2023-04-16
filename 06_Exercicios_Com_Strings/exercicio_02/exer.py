# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar 
# O seu nome e em seguida mostre o nome do usuário de trás para frente utilizando 
# Somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# Primeira formar 
nome = input("Digite seu nome: ").upper()

reverte_ordem = nome[::-1]

print(reverte_ordem)

# Segunda formar
nome = input("Digite seu nome: ").upper()

reverte_ordem = ''.join(reversed(nome))

print(reverte_ordem)