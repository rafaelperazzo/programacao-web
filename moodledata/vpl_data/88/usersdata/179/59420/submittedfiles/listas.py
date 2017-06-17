# -*- coding: utf-8 -*-
def alturas(a):
    for i in range(0,len(a),1):
        diferença=((a[i])-(a[i+1]))
    if diferença<0:
        diferença=diferença*(-1)
    else:
        diferença=diferença
    return (diferença)
b=[]
n=int(input('digite o valor de n :'))
for i in range(0,n,1):
    valor=int(input('digite o valor :'))
    b.append(valor)
c=alturas(b)
print(c)
            


