"""
Escreva um programa que leia um numero real e mostre na tela os valores de 25%, 50%, 75% do valor lido usando o formato com 3 casas decimais mostrado abaixo:
Exemplo Valor lido: 136.7
Exibir 25% -> 34.175 - 50% -> 68.350 - 75% -> 102.525
"""

numero = float(input("Digite um numero real: "))
percentual_25 = numero * 0.25
percentual_50 = numero * 0.5
percentual_75 = numero * 0.75
# metodo .format()
print("25% -> {} - 50% -> {} - 75% -> {}".format(round(percentual_25, 3), round(percentual_50, 3), round(percentual_75, 3)))
# metodo f-string
print(f"25% -> {round(percentual_25, 3)} - 50% -> {round(percentual_50, 3)} - 75% -> {round(percentual_75, 3)}")
# metodo printf
print("25%% -> %.3f - 50%% -> %.3f - 75%% -> %.3f" % (percentual_25, percentual_50, percentual_75))