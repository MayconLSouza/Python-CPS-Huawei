""""
Escreva um programa que leia 3 numeros inteiros e mostre na tela uma das seguintes opcoes:
a) Os 3 valores sao iguais
b) Ha 2 valores iguais e 1 diferente
c) Os 3 valores sao diferentes
"""

numeros = []

for i in range(3):
    numero = int(input("Digite um numero inteiro: "))
    numeros.append(numero)
  
if numeros[0] == numeros[1] == numeros[2]:
    print("Os 3 valores sao iguais")
else:
    if numeros[0] == numeros[1] or numeros[0] == numeros[2] or numeros[1] == numeros[2]:
        print("Ha 2 valores iguais e 1 diferente")
    else:
        print("Os 3 valores sao diferentes")
