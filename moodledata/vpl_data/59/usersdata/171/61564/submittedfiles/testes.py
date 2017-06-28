# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def correspondente(a,b):
    c=[]
    for i in range(0,len(a),1):
        if a[i] not in b:
            c.append(a[i])
    return(c)
n=int(input('digite numero de elementos:'))
a=[]
for i in range(0,n,1):
    valor=float(input('digite numeros para a:'))
    a.append(valor)
m=int(input('digite numero de elementos:'))
b=[]
for i in range(0,m,1):
    valor2=float(input('digite numeros para b:'))
    b.append(valor2)
print(consecutivos(a,b))
