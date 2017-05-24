# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
i=1
contador=0
for i in range (1,n+1,1):
    if i%a==0 or i%b==0:
        print(i)
        contador=contador+1
        i=i+1    
    
