# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
numerador=1
denominador=numerador*numerador
for i in range (1,n+1,1):
    x=numerador/denominador
    if i%2==0:
        soma=soma-x
    else:
        soma=soma+x
print('%.5f' %soma)        
    
