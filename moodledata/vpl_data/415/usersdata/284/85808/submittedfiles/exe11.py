# -*- coding: utf-8 -*-
n=int(input('digite um número de 8 algarismos: '))
if n>=100000000 or n<10000000:
    print('nao sei')
else:
    i=10000000
    s=0
    while(n//1):
        a=n//i
        s=s+a
        n=n%i
        i=i//10
    print(s)
        
    
           
       

   
   
    
    

    
        
    