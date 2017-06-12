# -*- coding: utf-8 -*-
x=int(input('digite o valor de x:'))
cont=0
soma=0
i=0

while x>0:
    resto=x%10
    soma=soma+(10**i)+resto
    x=x//2
    i=i+1
    cont=cont+1
print(cont)    
