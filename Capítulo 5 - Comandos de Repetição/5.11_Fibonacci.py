""""
Escreva um programa que leia uma quantidade Qtde e mostre na tela os Qtde primeiros termos da sequência de Fibonacci.
A sequência de Fibonacci é definida da seguinte forma: a) os dois primeiros termos da sequência são 0 e 1.
Do terceiro termo em diante cada termo é a soma dos dois anteriores.
Ex: Se Qtde = 9, então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21
"""
quantidade = int(input("Digite a quantidade de termos de fibonacci que deseja: "))
if quantidade <= 1:
    print(f"Quantidade inválida")
else:
    termos = 0
    fibonacci = 0
    proximo_fibonacci = 1
    while termos < quantidade:
        print(fibonacci, end=" ")
        termos += 1
        auxiliar = fibonacci + proximo_fibonacci
        fibonacci = proximo_fibonacci
        proximo_fibonacci = auxiliar
