"""
Em Albalandia mulheres e homens podem servir o exercito do pais.
O servico e opcional e e muito comum que as pessoas se apresentem para o servico em algum momento da vida.
Existe uma unica restricao para ingresso que e a idade da pessoa: para mulheres a idade aceita e entre 21 e 34 anos; para homens a idade aceita e entre 18 e 39 anos.
Escreva um programa que leia 3 dados de entrada: nome da pessoa, idade e sexo e informe se a pessoa sera aceita ou nao para o servico.
Para o sexo deve ser lido apenas 1 caractere que pode ser 'f' ou 'F' para feminino e 'm' ou 'M' para masculino, qualquer coisa diferente deve ser informado como invalido.
"""

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
sexo = input("Digite o sexo (F ou M): ").lower() # Converte para minusculas

if sexo not in ['f', 'm']:
    print("Sexo Invalido")
    exit()

if (sexo == 'f' and 21 <= idade <= 34) or (sexo == 'm' and 18 <= idade <= 39):
    print("Pedido Deferido")
else:
    print("Pedido Indeferido")