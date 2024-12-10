# Escreva um programa que leia um numero inteiro e mostre na tela se ele e divisivel por 10 ou nao.

numero = int(input("Digite um numero inteiro: "))

if (numero % 10) == 0:
    print("Divisivel por 10")
else:
    print("Nao divisivel por 10")