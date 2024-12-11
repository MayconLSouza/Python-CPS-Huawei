"""
Escreva um programa que permaneça em laço lendo cadeias de caracteres (strings).
Para cada cadeia digitada o programa deve exibir a cadeia seguida da quantidade de caracteres que ela contém.
O programa termina quando for digitado "FIM" (em letras maiúsculas).
"""
cadeia = input("Digite uma cadeia de caracteres: ")
while cadeia != "FIM":
    tamanho = len(cadeia)
    print(f"A cadeia '{cadeia}' possui {tamanho} caracter(es)")
    cadeia = input("Digite uma cadeia de caracteres: ")


