"""
Escreva um programa que leia um número inteiro e informe se esse número é primo ou não.
Lembrando: um número primo é divisível apenas por 1 e por ele mesmo.
"""
N = int(input("Digite um número inteiro: "))

if N <= 1:
    print(f"O número {N} não é primo.")
else:
    cont = 0
    divisor = 1
    while divisor <= N:
        if N % divisor == 0:
            cont += 1
        divisor += 1

    if cont == 2:
        print(f"O número {N} é primo.")
    else:
        print(f"O número {N} não é primo.")


