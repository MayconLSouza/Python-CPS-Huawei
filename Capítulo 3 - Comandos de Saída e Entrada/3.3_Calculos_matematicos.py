"""
Escreva um programa que leia 3 numeros reais em objetos denominados A, B e C.
O programa deve calcular e mostrar na tela os resultados das formulas a seguir, usando 3 casas decimais.
R1 = A+B+C
R2 = A.B.C
R3 = 2.(A+B)-C
R4 = (A+B+C)/3
R5 = (2B+3C)/(5A)
R6 = A²+B²
Para testar seu programa considere: A = 22.65 B = –39.1 C = 18.115
R1 = 1.665
R2 = –16042.916
R3 = –51.015
R4 = 0.555
R5 = –0.211
R6 = 2041.832
"""

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
R1 = A+B+C
R2 = A*B*C
R3 = 2*(A+B)-C
R4 = (A+B+C)/3
R5 = (2*B+3*C)/(5*A)
R6 = pow(A, 2) + pow(B, 2)
# metodo .format()
print("R1 = {}".format(round(R1, 3)))
print("R2 = {}".format(round(R2, 3)))
print("R3 = {}".format(round(R3, 3)))
print("R4 = {}".format(round(R4, 3)))
print("R5 = {}".format(round(R5, 3)))
print("R6 = {}".format(round(R6, 3)))
# metodo f-string
print(f"R1 = {round(R1, 3)}")
print(f"R2 = {round(R2, 3)}")
print(f"R3 = {round(R3, 3)}")
print(f"R4 = {round(R4, 3)}")
print(f"R5 = {round(R5, 3)}")
print(f"R6 = {round(R6, 3)}")
# metodo printf
print("R1 = %.3f" % R1)
print("R2 = %.3f" % R2)
print("R3 = %.3f" % R3)
print("R4 = %.3f" % R4)
print("R5 = %.3f" % R5)
print("R6 = %.3f" % R6)
