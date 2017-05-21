# -*- coding: utf-8 -*-
n=float(input('digite n:'))
i=0
soma=0
q=n//10
while q>=0:
    resto=n%10
    soma=soma+resto*2**i
    print('%d'%soma)
    i=i+1
    n//10!=0
    

