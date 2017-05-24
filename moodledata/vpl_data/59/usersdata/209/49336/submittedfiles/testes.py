# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('n:'))
z=0
soma=0
while n>0:
    x=n%10
    s=x*(2**z)
    z=z+1
    soma=soma+s
    n=n//10
print(soma)
        
    