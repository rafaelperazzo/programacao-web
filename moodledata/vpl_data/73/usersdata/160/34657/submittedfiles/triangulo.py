# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))



if a<b+c:
    print('S')
    
elif (a**2)==(b**2)+(c**2):
     print ('Re')
     
elif (a**2)>(b**2)+(c**2):
        print('Ob')
        
elif (a**2)<(b**2)+(c**2):
     print('Ac')
        
elif a==b==c:
    print('Eq')
        
elif b==c!=a:
    print('Is')
        
elif a!=b!=c:
    print('Es')
        
else:
    print('N')
