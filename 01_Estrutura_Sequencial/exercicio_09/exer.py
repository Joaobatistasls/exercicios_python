# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

temperatura_fahre = int(input("Informe a temperatura em graus Fahrenheit: "))

converte_celsius = 5 * ((temperatura_fahre - 32) / 9)

print("Sua temperatura em graus Celsius é : {}".format(converte_celsius))