"""
Escreva um programa que permaneça em laço enquanto um valor inteiro lido for diferente de zero.
Totalize e conte os valores digitados, exceto o zero, e apresente esses valores na tela.
Totalizar é somar os valores.
"""
soma = quantidade = 0
valor = int(input("Digite um valor inteiro: "))

while valor != 0:
    quantidade += 1
    soma += valor
    valor = int(input("Digite um valor inteiro: "))

print(f"Soma = {soma}")
print(f"Quantidade de valores digitados = {quantidade}")
