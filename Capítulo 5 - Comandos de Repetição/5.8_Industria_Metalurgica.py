"""
Uma indústria metalúrgica adota um código de produto com o seguinte formato TMMM, onde T indica o uso do produto, sendo 1 para residencial; 2 para industrial e MMM indica qual é o produto.
Escreva um programa que permaneça em laço até que seja digitado 0. Em cada repetição leia duas informações:
a)O código do produto;
b)A quantidade vendida desse produto
O programa deve totalizar separadamente e exibir na tela as quantidades de produtos residenciais e industriais vendidos. Se o dígito T do código não for 1 ou 2 deve ser mostrado "Tipo Inválido" e a quantidade deve ser ignorada.
"""
produto_residencial = produto_industrial = 0
codigo_produto = int(input("Digite o código do produto (TMMM): "))
while codigo_produto != 0:
    quantidade_vendida = int(input(f"Digite a quantidade vendida do produto {codigo_produto}: "))
    T = codigo_produto // 1000
    if T == 1:
        produto_residencial += quantidade_vendida
    elif T == 2:
        produto_industrial += quantidade_vendida
    else:
        print("Tipo inválido")
    codigo_produto = int(input("Digite o código do produto (TMMM): "))

print(f"Quantidade vendida de produtos residenciais = {produto_residencial}")
print(f"Quantidade vendida de produtos industriais = {produto_industrial}")