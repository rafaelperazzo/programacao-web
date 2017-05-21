# -*- coding: utf-8 -*-
n=int(input('digite n:'))
cont=0


for i in range (2,n,1):
    if n%i==1:
        print(i)
        cont=cont+1
    
    if cont==0:
        print('n primo')
        
    
    
    if cont==1:
        print('primo')