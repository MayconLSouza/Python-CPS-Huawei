"""
Escreva um programa que leia a idade de uma pessoa e indique qual sua classe eleitoral:
a) menor que 16 anos -> nao eleitor
b) entre 18 completos e 65 anos incompletos -> eleitor obrigatorio
c) entre 16 anos completos e 18 anos incompletos ou 65 anos completos -> eleitor facultativo
"""

idade = int(input("Digite a idade: "))

if idade < 16:
    print("Nao eleitor")
elif 18 <= idade < 65:
    print("Eleitor obrigatorio")
else:
    print("Eleitor facultativo")