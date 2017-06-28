# -*- coding: utf-8 -*-
def alturas(a):
    diferença=0
    degrais=0
    for i in range(0,len(a)-1,1):
        diferença=(a[i]-a[i+1])
    if diferença<0:
        diferença=diferença*(-1)
    if diferença>degrais:
        degrais=diferença
    return (degrais)
n=int(input('digite o valor de n :'))
b=[]
for i in range(0,n,1):
    valor=int(input('digite o valor :'))
    b.append(valor)
c=alturas(b)
print(c)
            


