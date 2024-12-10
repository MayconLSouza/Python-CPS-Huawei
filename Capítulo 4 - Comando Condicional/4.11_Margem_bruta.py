"""
No comercio, o conceito de Margem Bruta e uma porcentagem que e aplicada ao preco de custo para se obter o preco de venda.
Uma loja tem como politica comercial aplicar uma margem bruta de 45% quando o preco de custo de um produto e menor ou igual a R$ 100,00.
Se o produto custa mais que isso a margem bruta e de 35%.
Escreva um programa que leia o preço de custo do produto e mostre na tela qual o seu preço de venda, com duas casas decimais.
"""

preco_custo = float(input("Digite o preco de custo do produto (R$): "))
if preco_custo <= 100.00:
    preco_venda = (preco_custo * 0.45) + preco_custo
    print(f"O preco de venda do produto e R$ {round(preco_venda, 2)}")
else:
    preco_venda = (preco_custo * 0.35) + preco_custo
    print(f"O preco de venda do produto e R$ {round(preco_venda, 2)}")