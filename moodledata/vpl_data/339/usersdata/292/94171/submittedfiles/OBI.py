# -*- coding: utf-8 -*-
n = int(input("Digite o número de competidores: "))
p = int(input("Digite o número mínimo de pontos para ser classificado: "))
f1, f2, cont = [], [], 0

for i in range(1, n+1):
    f1.append(int(input("Digite a pontuação do %dº competidor na fase 1: "%i)))
    f2.append(int(input("Digite a pontuação do %dº compedidor na fase 2: "%i)))
del n

for i in range(0, len(f1)):
    if (f1[i] + f2[i]) >= p:
        cont += 1
        
print(cont)