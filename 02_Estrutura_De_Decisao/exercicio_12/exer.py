# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação 
# sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 
# questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 
# 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


telefonou = input("Telefonou para a vítima? ")
esteve_local = input("Esteve no local do crime? ")
mora_perto = input("Mora perto da vítima? ")
devia_vitima = input("Devia para a vítima? ")
trabalhou_vitima = input("Já trabalhou com a vítima? ")

participou = 1

if (telefonou == "sim" or "s"):
    participou += 1

if (esteve_local == "sim" or "s"):
    participou += 1

if (mora_perto == "sim" or "s"):
    participou += 1

if (devia_vitima == "sim" or "s"):
    participou += 1

if (trabalhou_vitima == "sim" or "s"):
    participou += 1

if (participou == 2):
    print("Você é Suspeito!") 
elif (participou == 3 or participou == 4):
    print("Você é Cúmplice!")
elif (participou == 5):
    print("Você é o Assasino!")
else:
    print("Você é Inocente!")

    

