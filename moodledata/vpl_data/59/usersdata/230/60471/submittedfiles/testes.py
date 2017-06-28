# -*- coding: utf-8 -*-
import math
def feliz(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]**2
        if soma==1:
            return True
        else:
            return False
    return(soma)


a=[]
for i in range(0,n,1):
    n=int(input('Valor:'))
    a.append(n)
    
if feliz(a):
    print('Feliz')
else:
    print('Nao Feliz')