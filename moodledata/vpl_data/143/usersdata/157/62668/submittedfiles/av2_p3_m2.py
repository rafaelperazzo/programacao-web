# -*- coding: utf-8 -*-
def degrau (a,b):
    for i in range (1, n-1,1):
       b.append(a[i]-a[i+1])
    for i in range (0,len(b),1):
        if (b[i]<0):
            b[i]=b[i]*(-1)
    return(b)
        
n=int(input('Digite a quantidade de elementos: '))
a=[]
b[]
for i in range (0,n,1):
    valor=int(input('Valor da lista: '))
    a.append(valor)
print(degrau(a,b))
        