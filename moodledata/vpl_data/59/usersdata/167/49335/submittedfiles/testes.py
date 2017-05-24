# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
soma=0
i=0
while n>0:
    m=n%10
    soma=soma+(m*(2**i))
    n=n//10
    i=i+1
print(soma)
        
    