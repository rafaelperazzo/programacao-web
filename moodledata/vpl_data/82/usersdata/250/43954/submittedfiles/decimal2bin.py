# -*- coding: utf-8 -*-
n=int(input('digite n:'))
i=0
soma=0
while n//10>=0:
    resto=n%10
    soma=soma+(resto*(2**i))
    i=i+1
    print('%d'%soma)
    

