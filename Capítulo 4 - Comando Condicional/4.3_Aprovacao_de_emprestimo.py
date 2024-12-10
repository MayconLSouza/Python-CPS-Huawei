"""
Uma empresa financeira concede emprestimos a pessoas fisicas quando o valor da parcela e menor que 8% do salario da pessoa.
Escreva um programa que leia dois numeros reais: o valor do salario e o valor da parcela e informe se o emprestimo sera concedido ou nao.
"""

salario = float(input("Digite o valor do salario (R$): "))
parcela = float(input("Digite o valor da parcela (R$): "))

if parcela < (0.08 * salario):
    print("Emprestimo concedido")
else:
    print("Emprestimo nao concedido")