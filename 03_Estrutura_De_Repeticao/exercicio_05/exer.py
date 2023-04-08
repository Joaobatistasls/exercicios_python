# Altere o programa anterior permitindo ao usuário informar as 
# Populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = float(input("Informe a quantidade de habitantes do país A: "))
b = float(input("Informe a quantidade de habitantes do país B: "))
a_taxa_anual = float(input("Informe a taxa de crescimento anual do páis A: "))
b_taxa_anual = float(input("Informe a taxa de crescimento anual do páis B: "))
anos = 0

while (a < b):
    a = a + a * a_taxa_anual
    b = b + b * b_taxa_anual

    anos = anos + 1

    if (a >= b):
        print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a populaçõa do país B.")
        break

