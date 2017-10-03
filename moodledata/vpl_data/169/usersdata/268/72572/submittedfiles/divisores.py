# -*- coding: utf-8 -*-
import math

n=int(input('Digite a quantidade de multiplos: '))
a=int(input('Digite o numero a : '))
b=int(input('DIgite o numero b : '))
i=1
if (n%2)==0:
    while(i<=n/2):
             multiploa=a*i
             multiplob=b*i
             i= i + 1
             if (multiploa<multiplob):
                 print(multiploa)
                 print(multiplob)
             if (multiplob>multiploa):
                 print(multiplob)
                 print(multiploa)
             if(multiploa==multiplob):
                 print(multiploa)
else:
    if (a<=b):
        while(i<=(n//2)):
             multiploa=a*i
             print(multiploa)
             multiplob=b*i
             print(multiplob)
             i= i + 1
    
    if(a>b):
         while(i<=n//2):
             multiplob=b*i
             print(multiplob)
             multiplob=a*i
             print(multiploa)
             i= i + 1
    
if (n%2)!=0:
    if(a<=b):
        print(multiploa*i)
    else:
        print(multiplob*i)
   
  
   
  
  
  
  

        

