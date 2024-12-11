"""
Escreva um programa que obrigatoriamente leia um inteiro que esteja no intervalo fechado [100, 200].
Se o valor fornecido estiver fora do intervalo o programa deve avisar que o valor é inválido e permanecer no laço.
Quando um valor válido for fornecido o programa deve informar que o valor foi aceito e terminar.
"""
valor = int(input("Digite um valor inteiro que esteja no intervalo fechado [100, 200]: "))

while valor < 100 or valor > 200:
    print("Valor inválido")
    valor = int(input("Digite um valor inteiro que esteja no intervalo fechado [100, 200]: "))

print(f"O valor {valor} foi aceito")