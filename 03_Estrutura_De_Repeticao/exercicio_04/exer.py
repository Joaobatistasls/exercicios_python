# Supondo que a população de um país A seja da ordem de 80000 habitantes 
# Com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
# Habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
# E escreva o número de anos necessários para que a população do país A ultrapasse
# Ou iguale a população do país B, mantidas as taxas de crescimento.

a = 80000
b = 200000
a_taxa_anual = 0.3
b_taxa_anual = 0.015
anos = 0

while (a < b):
    a = a + a * a_taxa_anual
    b = b + b * b_taxa_anual

    anos = anos + 1

    if (a >= b):
        print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a populaçõa do país B.")
        break