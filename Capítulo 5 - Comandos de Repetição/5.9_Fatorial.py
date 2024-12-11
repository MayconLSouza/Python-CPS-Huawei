"""
Escreva um programa que leia um número inteiro N. Em seguida calcule e mostre na tela o fatorial de N (N!).
"""
N = int(input("Insira o valora para o cálculo fatorial: "))
while N <= 0:
    print("Valor inválido")
    N = int(input("Insira o valora para o cálculo fatorial: "))

fatorial = 1
cont = 1
while cont <= N:
    fatorial *= cont
    cont += 1

print(f"{N}! = {fatorial}")