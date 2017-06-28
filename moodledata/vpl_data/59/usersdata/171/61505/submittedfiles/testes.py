# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def lecker(a):
    cont=0
    for i in range(0,len(a),1):
        if i==0:
            if a[i]>a[i+1]:
                cont=cont+1
        elif i==len(a)-1:
            if a[i]>a[i-1]:
                cont=cont+1
        else:
            if a[i]>a[i+1] and a[i]>a[i-1]:
                cont=cont+1
    if cont==1:
        return True
    else:
        return False
n=int(input('digite numero de elementos da lista:'))
a=[]
for i in range(0,n,1):
    numero=int(input('digite numero á ser inserido na lista'))
    a.append(numero)
if lecker (a):
    print('sim')
else:
    print('n')