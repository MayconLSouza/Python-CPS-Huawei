"""
Escreva um programa que leia um número N e em seguida exiba na tela todos os números divisíveis por 7 entre 1 e N (inclusive).
"""
N = int(input("Digite um inteiro: "))
cont = 1
while cont <= N:
    if cont % 7 == 0:
        print(cont, end=" ")
    cont += 1
