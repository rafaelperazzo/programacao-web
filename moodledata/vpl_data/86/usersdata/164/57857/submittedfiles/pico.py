# -*- coding: utf-8 -*-

def subida(b):
    m=len(b)/2
    for j in range (0, m+1, 1):
        if (b[j]<b[j]+1):
            subida=True
        else:
            subida=False

def descida(c):
    m=len(c)/2    
    for k in range (m, len(c), 1):
        if (c[k]>c[k]+1):
            descida=True
        else:
            descida=False


n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
for z in range (1, n+1, 1):
    valor=float(input('Digite os elementos da lista: '))
    a.append(valor)
if (subida==True and descida==True):
    print('S')
else:
    print('N')

