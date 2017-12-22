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

for i in range(1,N,1):
    if (altura_lado_esq[i-1] > secoes[i]):
        altura_lado_esq[i] = altura_lado_esq[i-1]
    else:
        altura_lado_esq[i] = secoes[i]

for i in range(N-2,-1,-1):
    if (altura_lado_dir[i+1] > secoes[i]):
        altura_lado_dir[i] = altura_lado_dir[i+1]
    else:
        altura_lado_dir[i] = secoes[i]

secoes_cobertas = 0

for i in range(N):
    if (secoes[i] < altura_lado_esq[i] and secoes[i] < altura_lado_dir[i]):
        secoes_cobertas += 1

print(secoes_cobertas)