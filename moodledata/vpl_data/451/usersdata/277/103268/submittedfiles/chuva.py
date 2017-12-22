# -*- coding: utf-8 -*-
while(True):
    N = int(input('Digite o numero de secoes da piscina: '))
    if (N > 0 and N <= 10**5):
        break

piscina = []    
for i in range(N):
    while(True):
        H = int(input('Altura da secao %dª: ' % i))
        if (H > 0 and H <= 10**9):
            break
    piscina.append(H)

secoes_cobertas = 0
for i in range(1,N,1):
    if (i == 0):
        if (piscina[i] < piscina[i-1]):
            secoes_cobertas += 1
    else:
        if (piscina[i] <= piscina[i-1]):
            secoes_cobertas += 1

print(secoes_cobertas)
