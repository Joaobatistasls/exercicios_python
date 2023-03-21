# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print("[F] Feminino [M] Masculino")

letra_digitada = input("Me informe a letra desejada? ")

if (letra_digitada.upper() == "F"):
    print("F - Feminino")
elif (letra_digitada.upper() == "M"):
    print("M - Masculino")
else:
    print("Sexo invalido!!")

