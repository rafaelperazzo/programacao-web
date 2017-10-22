# -*- coding: utf-8 -*-
n=int(input('digite um número de 8 algarismos: '))
while( 99999999<n or n<10000000):
    print('nao sei')
    break

m=10**7
o=10
while( 99999999>=n and n>=10000000):
    if m<=10**7 and m>=1:
        q=n//m
        print(q)
    m=m/o
    n=n%m    
       
        
   
   
    
    

    
        
    