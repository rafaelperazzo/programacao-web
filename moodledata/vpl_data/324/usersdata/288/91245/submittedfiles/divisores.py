# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de multiplos n: '))
while n<=0:
    n=int(input('Digite um inteiro n: '))
a=int(input('Digite um inteiro a: '))
while a<=0:
    a=int(input('Digite um inteiro a: '))
b=int(input('Digite um interro b: '))
while b<=0:
    b=int(input('Digite um inteiro b: '))
cont=0
i=1
while cont<n:
    if i%a==0 or i%b==0:
        print (i)
        cont+=1
    i+=1
    
   

    


   
   