# -*- coding: utf-8 -*-
while(True):
    M = int(input('Digite o numero de quadras no sentido Norte-Sul: '))
    if (M >= 2 and M <= 1000):
        break

while(True):
    N = int(input('Digite o numero de quadras no sentido Leste-Oeste: '))
    if (N >= 2 and N <= 1000):
        break

quadras = []

for i in range(M):
    quadras_les_oes = []
    for j in range(N):
        while(True):
            V = int(input('Digite o valor da quadra em milhoes de reais: '))
            if (V >= 1 and V <= 100):
                break
        quadras_les_oes.append(V)
    quadras.append(quadras_les_oes)

menor_valor = 100*(M+1)

for j in range(N):
    for i in range(M):
        