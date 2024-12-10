"""
Escreva um programa para uma fabrica de calcados que leia o codigo LL de um calcado, que e um numero inteiro com 2 digitos.
Exiba na tela a linha do calcado, conforme a tabela a seguir.
Se o numero fornecido nao estiver na tabela, deve-se exibir a mensagem "Codigo invalido".
LL | Linha de calcados
16 | Bebe
23 | Infantil feminino
25 | Infantil masculino
29 | Infantil esportivo
42 | Masculino formal
43 | Masculino casual
49 | Masculino esportivo
52 | Feminino formal salto baixo
53 | Feminino formal salto alto
55 | Feminino casual salto baixo
56 | Feminino casual salto alto
59 | Feminino esportivo
"""

linhas_calcados = {
    16: "Bebe",
    23: "Infantil feminino",
    25: "Infantil masculino",
    29: "Infantil esportivo",
    42: "Masculino formal",
    43: "Masculino casual",
    49: "Masculino esportivo",
    52: "Feminino formal salto baixo",
    53: "Feminino formal salto alto",
    55: "Feminino casual salto baixo",
    56: "Feminino casual salto alto",
    59: "Feminino esportivo"
}

ll = int(input("Digite o codigo LL do calcado: "))

if ll in linhas_calcados:
    print(linhas_calcados[ll])
else:
    print("Codigo Invalido")
