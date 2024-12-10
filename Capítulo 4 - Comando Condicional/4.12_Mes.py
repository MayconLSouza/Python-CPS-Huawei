"""
Leia um numero inteiro entre 1 e 12 e exiba o mes correspondente.
Caso seja digitado um numero fora desse intervalo, o programa deve exibir uma mensagem informando que nao existe mes com este numero.
"""

meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes = int(input("Digite um numero inteiro (1-12): "))

if 1 <= mes <= 12:
    print(f"O mes correspondente e {meses[mes-1]}")
else:
    print(f"Nao existe mes correspondente ao numero {mes}")
