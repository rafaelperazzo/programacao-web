# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a= input('Digite o valor de a')
b= input('Digite o valor de b')
c= input('Digite o valor de c')
#PROCESSAMENTO
if a>=b and b>=c and c>0:
    soma = b+c
    if a<soma : 
        print ('S')
        bc= (b**2)+(c**2)
        aQ= a**2
        if aQ==bc :
            print ('Re')
        elif aQ>bc :
            print ('Ob')
        elif aQ<bc :
            print ('Ac')
            if a==b and b==c :
                print('Eq')
            elif b==c and c!=a :
                print('Is')
            elif a!=b and b!=c and a!=c:
                print('Es')
else:
    print('N')
                
    
