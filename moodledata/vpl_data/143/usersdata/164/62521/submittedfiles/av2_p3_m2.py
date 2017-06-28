# -*- coding: utf-8 -*-
def degrau (a, b):
    for i in range (1, len(a)-1, 1):
        dif=a[i]-a[i+1]
        if (dif<0):
            dif=dif*(-1)
        else:
            dif=dif*1
        b.append(dif)    
        return(b[])    
    
n=int(input('Quantidade de elementos: '))
a=[]
b=[]
for i in range (0, n, 1):
    valor=int(input('Valor da lista: '))
    a.append(valor)
print(degrau(a,b))
