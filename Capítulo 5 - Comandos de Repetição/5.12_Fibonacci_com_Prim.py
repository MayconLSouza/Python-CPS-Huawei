quantidade = int(input("Digite a quantidade de termos de fibonacci que deseja: "))
Prim = int(input('Digite o Prim: '))
print(f'Os {quantidade} primeiros termos da sequência de Fibonacci maiores que {Prim} são:')
termos = 0
fibonacci = 0
proximo_fibonacci = 1
while termos < quantidade:
    if fibonacci > Prim:
        print(fibonacci, end=" ")
        termos += 1
    auxiliar = fibonacci + proximo_fibonacci
    fibonacci = proximo_fibonacci
    proximo_fibonacci = auxiliar