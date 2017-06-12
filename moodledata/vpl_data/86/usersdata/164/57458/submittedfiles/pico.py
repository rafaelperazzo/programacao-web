# -*- coding: utf-8 -*-

def pico(b):
    o=len(b)
    m=len(b)//2
    for i in range (0, m+1, 1):
        if (len(b)<m+1):
            if (b[i]<b[j]+1):
                o=o
    for k in range (m, len(b), 1):    
        if (len(b)>m):
            if (b[k]>b[k]+1):
                o=o
        return True
    else:
        return False

n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
for z in range (1, n+1, 1):
    valor=float(input('Digite os elementos da lista: '))
    a.append(valor)
if (True):
    print('S')
else:
    print('N')

