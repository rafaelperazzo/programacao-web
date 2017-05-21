# -*- coding: utf-8 -*-
n=int(input('digite n:'))
i=0
soma=0
q=n//10
contador=0
while q>=0:
    resto=n%10
    soma=resto*2**i
    contador=contador+1
    print('%d'%soma)
    i=i+1
    

