"""
Escreva um programa que leia um numero inteiro que representa uma quantidade de tempo em segundos.
Calcule e mostre na tela a quantidade de horas, minutos e segundos.
Exemplos:
Entrada (segundos) | Saida
       1           | 0 hora(s), 0 minuto(s), 1 segundo(s)
      38           | 0 hora(s), 0 minuto(s), 38 segundo(s)
     746           | 0 hora(s), 12 minuto(s), 26 segundo(s)
    4578           | 1 hora(s), 16 minuto(s), 18 segundo(s)
   73551           | 20 hora(s), 25 minuto(s), 51 segundo(s)
"""

quantidade_tempo = int(input("Digite a quantidade de tempo em segundos: "))
tempo_horas = quantidade_tempo // 3600
quantidade_tempo %= 3600
tempo_minutos = quantidade_tempo // 60
tempo_segundos = quantidade_tempo % 60
# metodo .format()
print("{} hora(s), {} minuto(s), {} segundo(s)".format(tempo_horas, tempo_minutos, tempo_segundos))
# metodo f-string
print(f"{tempo_horas} hora(s), {tempo_minutos} minuto(s), {tempo_segundos} segundo(s)")
# metodo printf
print("%i hora(s), %i minuto(s), %i segundo(s)" % (tempo_horas, tempo_minutos, tempo_segundos))
