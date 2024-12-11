"""
Escreva um programa que leia três números inteiros: LMin, LMax e D.
Em seguida exiba na tela todos os valores divisíveis por D que estão dentro do intervalo fechado [LMin, LMax].
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
    exit()

D = int(input("Digite o divisor: "))
if D == 0:
    print("O divisor não pode ser 0")
    while D == 0:
        D = int(input("Digite o divisor: "))

cont = LMin + 1
while cont < LMax:
    if cont % D == 0:
        print(cont, end=" ")
    cont += 1
