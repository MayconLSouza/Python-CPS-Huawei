"""
Escreva um programa que leia os nomes de 3 pessoas de uma familia: mae, pai e crianca. O programa deve exibir na tela a mensagem.
"Os adultos {mae} e {pai} sao os responsaveis por {crianca}"
"""

mae = input("Digite o nome da mae: ")
pai = input("Digite o nome do pai: ")
crianca = input("Digite o nome da crianca: ")
# metodo .format()
print("Os adultos {} e {} sao os responsaveis por {}".format(mae, pai, crianca))
# metodo f-string
print(f"Os adultos {mae} e {pai} sao os responsaveis por {crianca}")
# metodo printf
print("Os adultos %s e %s sao os responsaveis por %s" % (mae, pai, crianca))