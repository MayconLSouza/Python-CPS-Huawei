"""
Classificacao indicativa e um conceito que se aplica a faixa etaria para a qual uma obra audiovisual se recomenda ou nao.
Suponha que um filme em cartaz no cinema tenha a Classificacao de 16 anos.
Escreva um programa que leia a idade de uma pessoa e mostre se esta de acordo ou nao com a classificacao.
"""

idade = int(input("Digite a idade: "))

if idade >= 16:
    print("Pode ver o filme")
else:
    print("Não pode ver o filme")