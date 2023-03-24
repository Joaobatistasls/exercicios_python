# Faça um Programa que peça um número correspondente a um 
# Determinado ano e em seguida informe se este ano é ou não bissexto.

dia_ano_atual = input("Informe quantos dias tem o ano atual? ")

if (dia_ano_atual == "365"):
    print("Esse ano não é bissexto!")
elif (dia_ano_atual == "366"):
    print("Esse é um ano bissexto!")
else:
    print("Valor Inválido!")