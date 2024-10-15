"""
Uma empresa comercial trabalha com 3 vendedores externos e os remunera com R$ 1200,00 fixos mais comissao de 6% sobre o valor total vendido no mes.
Escreva um programa que leia o nome e o total vendido pelos 3 vendedores, calcule e exiba na tela a mensagem de saida conforme o exemplo a seguir.
Exiba os valores numericos com duas casas decimais.
Exemplo de saida:
vendedor Jose Carlos Santos vendeu R$ 43759.35 e faz jus a uma comissao de R$ 3825.56
vendedor Manoel Guimaraes vendeu R$ 61417.81 e faz jus a uma comissao de R$ 4885.07
vendedor Plinio Pereira vendeu R$ 39336.87 e faz jus a uma comissao de R$ 3560.21
"""
nome_vendedor = [""] * 3
total_vendido = [0.0] * 3
comissao = [0.0] * 3

i = 0
while i < 3:
    nome_vendedor[i] = input("Digite o nome do vendedor: ")
    total_vendido[i] = float(input(f"Digite o valor total vendido (R$) no mes pelo vendedor {nome_vendedor[i]}: "))
    comissao[i] = 1200 + (total_vendido[i] * 0.06)
    i += 1

i = 0
while i < 3:
    # metodo .format()
    print("vendedor {} vendeu R$ {} e faz jus a uma comissao de R$ {}".format(nome_vendedor[i], round(total_vendido[i], 2), round(comissao[i], 2)))
    # metodo f-string
    print(f"vendedor {nome_vendedor[i]} vendeu R$ {round(total_vendido[i], 2)} e faz jus a uma comissao de R$ {round(comissao[i], 2)}")
    # metodo printf
    print("vendedor %s vendeu R$ %.2f e faz jus a uma comissao de R$ %.2f" % (nome_vendedor[i], total_vendido[i], comissao[i]))
    i += 1



