# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- 
# Noturno. Imprima a mensagem "Bom Dia!", 
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("[M] - Matutino [V] - Vespertino [N] - Nortuno")
turno = input("Em qual turno você estuda? ")

if (turno == "M" or turno == "Matutino"):
    print("Bom dia!")
elif (turno == "V" or turno == "Vespertino"):
    print("Boa tarde!")
elif (turno == "N" or turno == "Nortuno"):
    print("Boa noite!")
else:
    print("Valor Inválido!")

    