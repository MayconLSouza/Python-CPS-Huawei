"""
Escreva um programa que leia 3 numeros inteiros e mostre na tela se eles formam um triangulo ou nao.
Caso formem um triangulo informe o tipo de triangulo (equilatero, isosceles ou escaleno).
Regra: Para tres numeros formarem um triangulo precisa ocorrer que:
a) os 3 numeros precisam ser maiores que 0;
b) a soma dos 2 menores valores deve ser maior que o terceiro.
"""

lados = []
for i in range(3):
    lado = int(input("Digite um número inteiro: "))
    lados.append(lado)

# Os 3 numeros precisam ser maiores que 0
if any(lado <= 0 for lado in lados):
    print("Nao e Triangulo")
else:
    lados.sort()
    # A soma dos 2 menores valores deve ser maior que o terceiro
    if lados[0] + lados[1] > lados[2]:
        if lados[0] == lados[1] == lados[2]:
            print("Triangulo Equilatero")
        elif lados[0] == lados[1] or lados[1] == lados[2]:
            print("Triangulo Isosceles")
        else:
            print("Triangulo Escaleno")
    else:
        print("Nao e Triangulo")
