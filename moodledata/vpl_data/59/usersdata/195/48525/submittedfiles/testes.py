# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
contador=o
i=1
for i in range (1,n+1,1):
    if a%i==0 and b%i==0:
        print(i)
        contador=contador+1
    i=i+1    
    
