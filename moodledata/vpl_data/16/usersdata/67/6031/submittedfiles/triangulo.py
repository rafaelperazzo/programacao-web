# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input("Digite o valor de a:")
b=input("Digite o valor de b:")
c=input("Digite o valor de c:")
if a<b+c:
    print("'S'")
    if (a**2)==(b**2)+(c**2):
        print("'Re'")
    elif a**2>(b**2)+(c**2):
        print("'Ob'")
    elif a**2<(b**2)+(c**2):
         print("'Ac'")
    if a==b==c:
        print("'Eq'")
    
            
    elif b==c!=a:
        print("'Is'")
    
           
    elif a!=b!=c:
        print("'Es'")
else: 
    print("'N'")
     
     

        

    