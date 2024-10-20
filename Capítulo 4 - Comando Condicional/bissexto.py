"""
Escreva um programa que leia um numero inteiro que representa um ano. Informe se esse ano e bissexto ou nao.
Regra: O ano e bissexto se cumprir uma das seguintes condicoes:
a) ser multiplo de 4 e ao mesmo tempo nao ser multiplo de 100
d) ser multiplo de 400
"""

ano = int(input("Digite o ano: "))

if (ano % 400) == 0:
    print("Ano Bissexto")
else:
    if ((ano % 4) == 0) and ((ano % 100) != 0):
        print("Ano Bissexto")
    else:
        print("Ano Comum")