# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
soma=0
i=0
while n>0:
    x=n%2
    n=n//2
    z=x*10**i
    soma=soma+z
    i=i+1
print(soma)
    
    