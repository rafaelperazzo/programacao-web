# -*- coding: utf-8 -*-
def quantidade (a,b):
    cont=o
    for i in range (o,len(a),1):
        if a[i] in b:
            cont=cont+1
        return(cont)
tn=int(input('digite n:'))
n=[]
for i in range(1,tn+1,1):
    valor=int(input('digite o valor:'))
    n.append(valor)
tm=int(input('digite m:'))
m=[]
for i in range(1,tm+1,1):
    valor=int(input('digite o valor:'))
    m.append(valor)
print(quantidade (a,b))
            
