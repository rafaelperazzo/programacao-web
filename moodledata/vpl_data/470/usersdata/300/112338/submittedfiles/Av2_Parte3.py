# -*- coding: utf-8 -*-
m = int(input('Digite o valor de m: '))
n = int(input('Digite o valor de n: '))
a = []
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(float(input('Digite um elemento: ')))
    a.append(linha)
    
def media(a,m):
    media = sum(a[m]) / len(a[m])
    return media
    
def dv(a,m,n):
    media = sum(a[m]) / len(a[m])
    soma = 0
    for i in range(0,n,1):
        soma = soma +((a[m][i] - media)**2)
    dv = ((1/(n-1)) * soma)**0.5
    return dv
    
for i in range(0,m,1):
    print ('%.2f' % media(a,i))
    print ('%.2f' % dv(a,i,n))
    
    
    

        
