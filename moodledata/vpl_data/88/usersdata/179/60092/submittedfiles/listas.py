# -*- coding: utf-8 -*-
def degrais(a):
    diferença=0
    degrau=0
    for i in range(0,len(a)-1,1):
        diferença=(a[i]-a[i+1])
        if diferença<0:
            diferença=diferença*(-1)
        if diferença>degrau:
            degrau=diferença
    return (degrau)
n=int(input('digite o valor de n :'))
b=[]
for i in range(0,n,1):
    valor=int(input('digite o valor :'))
    b.append(valor)
c=degrais(b)
print(c)
            


