# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
denominador=numerador*numerador
x=numerador/denominador
for i in range (1,n+1,1):
    if i%2==0:
        soma=soma-x
    else:
        soma=soma+x
print(soma)        
    
