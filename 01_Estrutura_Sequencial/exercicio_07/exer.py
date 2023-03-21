# Faça um Programa que calcule a área de um
# Quadrado, em seguida mostre o dobro desta área para o usuário.

quadrado = int(input("Qual a área do quadrado? "))

area_quadrado = quadrado ** 2
print("A área do seu quadrado é: {}".format(area_quadrado))

dobro_area_quadrado = area_quadrado * 2
print("O dobro da sua área é: {}".format(dobro_area_quadrado))