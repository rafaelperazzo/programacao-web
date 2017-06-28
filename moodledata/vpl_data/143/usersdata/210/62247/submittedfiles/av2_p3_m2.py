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
    return degrau
h=int(input('digite o valor de h:'))
j=[]
for i in range(0,h,1):
    numero=int(input('digite o numero:'))
    j.append(numero)
x=degrais(j)
print(x)
        
    