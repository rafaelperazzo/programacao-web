# -*- coding: utf-8 -*-
n=int(input('Informe o número de termos:'))
s=0
numerador=1
denominador=1
for i in range(1,n+1,1):
    if i%2==0:
        s=s-(numerador/denominador)
        numerador=numerador+1
        denominador=(numerador)**2
    else:
        s=s+(numerador/denominador)
        numerador=numerador+1
        denominador=(numerador)**2
print('%.5d' %s)    
