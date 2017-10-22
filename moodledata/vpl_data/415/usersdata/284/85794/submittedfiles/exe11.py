# -*- coding: utf-8 -*-
a=int(input('digite um número de 8 algarismos: '))


i=0
soma=0
while (a>=10000000 and a<=99999999):
    if a>0:
        
        n=a%10
        a=a//10
        i=i+1
        soma=soma+n
        if i==8:
            print(soma)
        else:
             
             print('nao sei')
           
       

   
   
    
    

    
        
    