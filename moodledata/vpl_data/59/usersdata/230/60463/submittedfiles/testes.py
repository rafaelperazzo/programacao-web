# -*- coding: utf-8 -*-
import math
def feliz(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]**2
        while(i>1):
            soma=soma+a[i]**2
            if soma==1:
                return True
            else:
                return False

n=int(input('Digite valor: '))
a=feliz(n)
if feliz(a):
    print('Feliz')
else:
    print('Nao Feliz')