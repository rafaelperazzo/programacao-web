# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite o comprimento do lado "a": '))
b=int(input('Digite o comprimento do lado "b": '))
c=int(input('Digite o comprimento do lado "c": '))

if(a>=b>=c>0):
      
      print('S')
      
      elif (a**2==b**2 + c**2):
         print('Re')

      elif (a**2>b**2 + c**2):
         print('Ob')

      elif (a**2<b**2 + c**2):
         print('Ac')
    

      elif (a==b==c):
         print('Eq')
    
      elif (b==c!=a):
        print('Is')
    
      elif (a!=b!=c):
        print('Es')
    
else:
    print('N')
    