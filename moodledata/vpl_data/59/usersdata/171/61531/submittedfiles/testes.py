# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/(len(a))
    return(media)
n=int(input('digite numero de elementos da lista:'))
a=[]
for i in range(0,n,1):
    numero=float(input('digite numero á ser inserido na lista:'))
    a.append(numero)
print('%.3f'%a[0])
print('%.3f'%a[len(a)-1])
print'%.3f'%(media(a))
print(a)