# -*- coding: utf-8 -*-
import math
def feliz(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]**2
        if soma!=1:
            return False
        else:
            return True

n=int(input('Digite valor: '))
a=[]
for i in range(0,n,1):
    a.append(n)
if feliz(a):
    print('Feliz')
else:
    print('Nao Feliz')