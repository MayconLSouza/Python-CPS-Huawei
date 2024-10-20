"""
Nas eleicoes municipais os municipios com 200 mil eleitores ou mais tem segundo turno caso o primeiro colocado nao tenha mais do que 50% dos votos.
Escreva um programa que leia o nome do municipio, a quantidade de eleitores e a quantidade de votos do candidato mais votado e informe se havera segundo turno ou nao.
"""

municipio = input("Digite o nome da cidade: ")
qtd_eleitores = int(input(f"Digite a quantidade de eleitores de {municipio}: "))
qtd_votos = int(input("Digite a quantidade de votos do candidato mais votado: "))

if qtd_eleitores >= 200000:
    if qtd_votos < (qtd_eleitores * 0.5):
        print(f"A cidade de {municipio} tera segundo turno")
    else:
        print(f"A cidade de {municipio} nao tera segundo turno")
else:
    print(f"A cidade de {municipio} nao pode ter segundo turno")
