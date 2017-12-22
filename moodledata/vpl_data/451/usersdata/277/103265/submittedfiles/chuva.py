# -*- coding: utf-8 -*-
while(True):
    N = int(input('Digite o numero de secoes da piscina: '))
    if (N > 0 and N <= 10**5):
        break
piscina = []    
for i in range(N):
    while(True):
        H = int(input('Altura da secao %d' % i))
        if (H > 0 and H <= 10**9):
            break
    piscina.append(H)
    
