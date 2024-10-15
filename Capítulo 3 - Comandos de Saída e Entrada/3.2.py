"""
Escreva um programa que leia um texto e mostre na tela o texto e a quantidade de caracteres que ele contem, usando a seguinte mensagem:
"O texto {AquiColoqueOTexto} contem {Quantidade} caracteres"
"""

texto = input("Digite o texto: ")
tamanho = len(texto)
# metodo .format()
print("O texto '{}' contem {} caracteres".format(texto, tamanho))
# metodo f-string
print(f"O texto '{texto}' contem {tamanho} caracteres")
# metodo printf
print("O texto %s contem %i caracteres" % (texto, tamanho))