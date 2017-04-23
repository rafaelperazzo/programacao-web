# -*- coding: utf-8 -*-
n=int(input('digite n:'))
contador=n
for i in range(n,1,n-1):
     contador=contador*i
     contador=contador*contador 
    print(contador)