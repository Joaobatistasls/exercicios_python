# Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando 
# A pedir as informações.

inicio = 1
tentativas = 100

while (inicio <= tentativas):
    nome_usuario = input("Informe um nome de usuário: ")
    senha_usuario = input("Informe uma sehas: ")

    if (nome_usuario == senha_usuario):
        print("Sua senha não pode ser igual ao usuário. ERRO!")
        continue
    else:
        print("Usuário e Senha cadastrado no sistema!")
        break

    inicio += 1

    