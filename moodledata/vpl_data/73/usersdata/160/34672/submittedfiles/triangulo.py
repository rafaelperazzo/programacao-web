# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))

a>=b>=c>0

if a<b+c:
    print('S')
    
    if (a**2)==(b**2)+(c**2):
     print ('Re')
     
if (a**2)>(b**2)+(c**2):
        print('Ob')
        
if (a**2)<(b**2)+(c**2):
     print('Ac')
        
if a==b==c:
    print('Eq')
        
if b==c!=a:
    print('Is')
        
if (a!=b) and (b!=c):
    print('Es')
    
else:
    print('N')
        

        
