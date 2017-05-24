# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
for numerador in range (1,n+1,1):
    x=numerador/(numerador*numerador)
    if numerador%2!=0:
        soma=soma+x
    else:
        soma=soma-x
print('s: %.5f' %soma)        
    
