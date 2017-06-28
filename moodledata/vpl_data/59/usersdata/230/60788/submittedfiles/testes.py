# -*- coding: utf-8 -*-
import math
def feliz(a):
    while a!=1:
        soma=0
        for i in range(0,len(a),1):
            soma=soma+(a[i])**2
            soma=a
            if soma==1:
                return True
            else:
                return False
    
    
n=int(input('Digite valor: '))
a=[]
for i in range(0,n,1):
    a.append(n)
if feliz(a):
    print('Feliz')
else:
    print('Nao Feliz')