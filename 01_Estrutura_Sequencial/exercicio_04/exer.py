# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

for nota in range(1, 6):
        # Inputs para fazer as pergunstas:
    bimestre_1 = input("Me informe a sua nota do 1° bimestre: ")
    bimestre_2 = input("Me informe a sua nota do 2° bimestre: ")
    bimestre_3 = input("Me informe a sua nota do 3° bimestre: ")
    bimestre_4 = input("Me informe a sua nota do 4° bimestre: ")

    # Int para inverte o type dos inputs:
    bimestre_1_nota = int(bimestre_1)
    bimestre_2_nota = int(bimestre_2)
    bimestre_3_nota = int(bimestre_3)
    bimestre_4_nota = int(bimestre_4)

    # Verificação para as notas bimestrais não serem maior que 10 e nota final:
    bimestre_1_maior = bimestre_1_nota > 10
    bimestre_2_maior = bimestre_2_nota > 10
    bimestre_3_maior = bimestre_3_nota > 10
    bimestre_4_maior = bimestre_4_nota > 10

    notas_final = (bimestre_1_nota + bimestre_2_nota + bimestre_3_nota + bimestre_4_nota) / 4

    # Verificação para vê sea nota final é maior que 10 e se o aluno foi aprovado
    if(notas_final > 10):
        print("Sua nota bimestral dever ser entre 0 é 10!")
        continue
    
    if(notas_final >= 6):
        print(f"Parabéns sua nota foi: {notas_final}")
        break
    else:
        print(f"Precisa melhorar, sua nota ficou abaixo da média e ela foi: {notas_final}")

print("Fim de ano!!")
