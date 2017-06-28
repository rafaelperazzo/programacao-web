# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def crescente(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]<a[i-1]:
            cont=cont+1
    if cont==len(a)-1:
        return True
    else:
        return False
n=int(input('digite n:'))
a=[]
for i in range(0,n,1):
    numero=float(input('digite n:'))
    a.append(numero)
if crescente(a):
    print('crescente')
else:
    print('nao e crescente')