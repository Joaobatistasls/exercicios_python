# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue 
# Pedindo até que o usuário informe um valor válido.

tentativas = 100

for nota_atual in range(1, tentativas + 1):
    peca_nota = input("Me informe uma nota entre 0 e 10: ")
    nota = int(peca_nota)

    if (nota < 0 or nota > 10):
        print("Você deve digitar um número entre 0 e 10!")
        continue
    else:
        print(f"Sua nota foi {nota}!")
        break

    