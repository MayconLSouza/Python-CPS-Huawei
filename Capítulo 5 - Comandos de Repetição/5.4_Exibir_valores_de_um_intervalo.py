"""
Escreva um programa que leia dois números inteiros: LMin e LMax.
Em seguida exiba na tela todos os valores dentro do intervalo fechado [LMin, LMax].
"""
LMin = int(input("Digite o valor mínimo do intervalo: "))
LMax = int(input("Digite o valor máximo do intervalo: "))

if LMin > LMax:
    print("Valores inválidos")
    while LMin > LMax:
        LMin = int(input("Digite o valor mínimo do intervalo: "))
        LMax = int(input("Digite o valor máximo do intervalo: "))

if LMin == LMax:
    print("Valores iguais")

cont = LMin + 1
while cont < LMax:
    print(cont, end=" ")
    cont += 1


