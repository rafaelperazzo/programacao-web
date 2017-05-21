# -*- coding: utf-8 -*-
n=int(input('digite um a valor:'))
i=0
soma=o
while n//2==0:
    resto=n%2
    soma=soma+(resto*(10**i))
    n=n//2
    i=i+1
    print('%d'%soma)
    

