# -*- coding: utf-8 -*-
def degrais(a,b):
    for i in range(0,n-1,1):
        b.append(a(i)-a(i-1))
    for i in range(0, len(b),1):
        if (b[i]<0):
            b[i]=b[i]*(-1)
    return(b)

n=int(input('NUMERO DE ELEMENTOS:'))
a=[]
b=[]
for i in range (0,n,1):
    valor=int(input('LISTA:'))
    a.append(valor)
print(degrais(a,b))
   