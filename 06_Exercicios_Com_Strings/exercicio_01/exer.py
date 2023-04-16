# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo
# Delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

string_um = "Brasil Hexa 2006"
string_dois = "Brasil! Hexa 2006!"

qt_string_um = len(string_um)
qt_string_dois = len(string_dois)

print(string_um)
print(string_dois)

print("Tamanho de 'Brasil Hexa 2006': {} caracteres".format(qt_string_um))

print("Tamanho de 'Brasil! Hexa 2006!': {} caracteres".format(qt_string_dois))

if (qt_string_um == qt_string_dois):
  print("As duas string são do mesmo tamanho.")
else: 
  print("As duas strings são de tamanhos diferentes.")

if (string_um == string_dois):
  print("As duas string possue o mesmo conteúdo.")
else:
  print("As duas strings possuem conteúdo diferente.")