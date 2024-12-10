"""
Em um determinado momento do dia a cotacao de compra das moedas estrangeiras e a seguinte:
Dolar: US$ 1.00 = R$ 4.89 - Euro: € 1.00 = R$ 5.26 - Libra Esterlina: £ 1.00 = R$ 6.17
Escreva um programa que leia o tipo (D, E ou L maiusculo) e o valor de moeda estrangeira que se quer comprar e calcule o valor em reais necessarios.
"""

moeda = input("Digite a moeda estrangeira (USD, EUR, GBP): ").upper()
valor = float(input(f"Digite o valor de moeda estrangeira ({moeda}) que se quer comprar: "))

if moeda == "USD":
    valor_convertido = valor * 4.89
    print(f"\n{valor} {moeda} = {valor_convertido:.2f} BRL")
    print(f"Taxa de câmbio utilizada: 1 {moeda} = 4.89 BRL")
elif moeda == "EUR":
    valor_convertido = valor * 5.26
    print(f"\n{valor} {moeda} = {valor_convertido:.2f} BRL")
    print(f"Taxa de câmbio utilizada: 1 {moeda} = 5.26 BRL")
elif moeda == "GBP":
    valor_convertido = valor * 6.17
    print(f"\n{valor} {moeda} = {valor_convertido:.2f} BRL")
    print(f"Taxa de câmbio utilizada: 1 {moeda} = 6.17 BRL")
else:
    print("Moeda invaldia")


