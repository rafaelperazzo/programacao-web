# -*- coding: utf-8 -*-
while(True):
    N = int(input('Digite o numero de secoes da piscina: '))
    if (N > 0 and N <= 10**5):
        break

secoes = []
altura_lado_esq = []
altura_lado_dir = []
for i in range(N):
    while(True):
        H = int(input('Altura da secao: '))
        if (H > 0 and H <= 10**9):
            break
    secoes.append(H)
    altura_lado_esq.append(-1)
    altura_lado_dir.append(-1)

altura_lado_esq[0] = secoes[0]
altura_lado_dir[N-1] = secoes[N-1]
secoes_cobertas = 0
for i in range(1,N,1):
    if (i == 0):
        if (piscina[i] < piscina[i-1]):
            secoes_cobertas += 1
    else:
        if (piscina[i] <= piscina[i-1]):
            secoes_cobertas += 1

print(secoes_cobertas)
