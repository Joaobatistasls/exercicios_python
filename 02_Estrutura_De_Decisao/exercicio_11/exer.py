# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print("1- Domingo, 2- Segunda, 3- Terça, 4- Quarta, 5- Quinta, 6- Sexta, 7- Sábado")

dia_da_semana = input("Informe um dia da semana: ")

if (dia_da_semana == "Domingo" or dia_da_semana == "1"):
    print("Hoje é Domingo!")
elif (dia_da_semana == "Segunda" or dia_da_semana == "2"):
    print("Hoje é Segunda!")
elif (dia_da_semana == "Terça" or dia_da_semana == "3"):
    print("Hoje é Terça!")
elif (dia_da_semana == "Quarta" or dia_da_semana == "4"):
    print("Hoje é Quarta!")
elif (dia_da_semana == "Quinta" or dia_da_semana == "5"):
    print("Hoje é Quinta!")
elif (dia_da_semana == "Sexta" or dia_da_semana == "6"):
    print("Hoje é Sexta!")
elif (dia_da_semana == "Sábado" or dia_da_semana == "7"):
    print("Hoje é Sábado!")
else:
    print("Valor Inválido!")

    