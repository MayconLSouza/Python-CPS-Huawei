"""
Escreva um programa que leia o nome de um aluno e as notas obtidas em 3 avaliacoes.
A media final e a media aritmetica das 3 notas e a pessoa estara aprovada se essa media for maior ou igual a 7.0.
Mostre na tela o nome, a media e a situacao que sera "Aprovado" ou "Reprovado".
"""

nome_aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1+nota_2+nota_3) / 3

print(f"Aluno: {nome_aluno}")
print(f"Media: {media}")
if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")