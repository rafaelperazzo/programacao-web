# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
i=0
q=n//10
while q>=0:
    resto=n%10
    soma=resto*2**i
    print('%d'%soma)
    i=i+1
    

