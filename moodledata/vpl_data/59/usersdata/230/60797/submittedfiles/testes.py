# -*- coding: utf-8 -*-
import math
def feliz(a):
    while a!=1:
        soma=0
        for i in range(0,len(a),1):
            soma=soma+(a[i])**2
            a=soma
            if a==1:
                return True
            else:
                return False
    
    
n=int(input('Digite valor: '))
a=[]
while(n!=0) :
    a.append(n%10)
    n=n//10
if feliz(a):
    print('Feliz')
else:
    print('Nao Feliz')