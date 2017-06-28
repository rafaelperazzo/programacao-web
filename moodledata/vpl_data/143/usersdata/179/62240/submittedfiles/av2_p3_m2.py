# -*- coding: utf-8 -*-
def degrais(a):
    degrau=0
    for i in range(0,len(a)-1,1):
        diferença=a[i]-a[i+1]
        if diferença<0:
            diferença=diferença*(-1)
        if diferença>degrau:
            degrau=diferença
    return degrau
n=int(input('digite o valor de n :'))
b=[]
for i in range(0,n,1):
    numero=int(input('digite o numero :'))
    b.append(numero)
x=degrais(b)
print(x)