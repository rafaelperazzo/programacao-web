# -*- coding: utf-8 -*-
import math
def feliz(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]**2
        

n=int(input('Digite valor: '))
b=feliz(n)
if feliz(b):
    print('Feliz')
else:
    print('Nao Feliz')