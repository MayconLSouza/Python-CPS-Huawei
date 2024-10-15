"""
Quando uma pessoa ou uma empresa realiza um investimento espera-se um retorno positivo (lucro), embora tambem possa ocorrer um retorno negativo (prejuizo).
Uma forma inicial de avaliar o retorno e conhecida como Retorno sobre Investimento (ou ROI, uma sigla em ingles). Calculo do ROI:
𝑅𝑂𝐼 = (𝑅𝑒𝑐𝑒𝑖𝑡𝑎 − (𝐶𝑢𝑠𝑡𝑜𝑠 + 𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜)) . 100% / (𝐶𝑢𝑠𝑡𝑜𝑠+𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜)
Escreva um programa que leia 3 dados de entrada reais: Investimento, Custos e Receita, calcule o ROI usando a formula acima e exiba o resultado com uma casa decimal no formato mostrado abaixo.
Exemplo: Investimento = 2300.00 ; Custos = 345.73 ; Receita = 2712,17
Saída: ROI = 2.5%
Outros testes:
Investimento | Custos | Receita  |   ROI
  22500.00   | 535.83 | 25419.61 |  10.3%
  15000.00   | 419.35 | 14403.44 |  -6.6%
  18000.00   | 837.40 | 19132.28 |   1.6%
"""

investimento = float(input("Digite o valor de investimento (R$): "))
custo = float(input("Digite o valor de custo (R$): "))
receita = float(input("Digite o valor de receita (R$): "))
roi = ((receita-(custo+investimento))/(custo+investimento)) * 100
# metodo .format()
print("ROI = {}%".format(round(roi, 1)))
# metodo f-string
print(f"ROI = {round(roi, 1)}%")
# metodo printf
print("ROI = %.1f %%" % roi)

