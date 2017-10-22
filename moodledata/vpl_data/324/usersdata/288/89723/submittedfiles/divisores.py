# -*- coding: utf-8 -*-
import math
a=int(input('Digite um inteiro a: '))
b=int(input('Digite um interro b: '))
n=int(input('Digite a quantidade de multiplos n: '))
q=1
i=0
while i<n:
    if q%a==0 or q%b==0:
        print (q)
        i+=1
    q+=1

    


   
   