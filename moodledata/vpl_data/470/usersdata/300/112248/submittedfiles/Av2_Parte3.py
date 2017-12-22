# -*- coding: utf-8 -*-
m = int(input('Digite o valor de m: '))
n = int(input('Digite o valor de n: '))
a = []
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input('Digite um elemento: ')))
    a.append(linha)
    
def mdv(a,m):
    for i in range(0,m,1):
        media = sum(a[i]) / m
        cont = 0
        for j in range(0,m,1):
            soma = soma +((a[j] - media)**2)
        dv = ((1/(n-1)) * soma)**0.5
    media = float(media)
    dv = float(dv)
    return media
    return dv
    
for i in range(0,m,1):
    print ('%2f' % a[i])
    
    

        
