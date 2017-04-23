# -*- coding: utf-8 -*-
n=int(input('numero n'))
contador=0
i=2
while i<n:
    if n%i==0:
        contador=contador+1
        print(i)
    i=i+1
if contador==0:
    print(primo)
else:
    print(não primo)
        
    
