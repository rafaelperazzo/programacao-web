# -*- coding: utf-8 -*-
from __future__ import division
import math

x1 = input('Digite x1: ')
x2 = input('Digite x2: ')
x3 = input('Digite x3: ')
x4 = input('Digite x4: ')
x5 = input('Digite x5: ')
x6 = input('Digite x6: ')
x7 = input('Digite x7: ')
x8 = input('Digite x8: ')
x9 = input('Digite x9: ')


cont1=0
if x1==x2 and x2==x3 and x3==0:
    cont1=1

elif x4==x5 and x5==x6 and x6==0:
    cont1=1
elif x7==x8 and x8==x9 and x9==0:
    cont1=1
elif x1==x4 and x4==x7 and x7==0:
    cont1=1
elif x2==x5 and x5==x8 and x8==0:
    cont1=1
elif x3==x6 and x6==x9 and x9==0:
    cont1=1
elif x1==x5 and x5==x9 and x9==0:
    cont1=1
elif x3==x5 and x5==x7 and x7==0:
    cont1=1
    
cont2=0
if x1==x2 and x2==x3 and x3==1:
    cont2=1

elif x4==x5 and x5==x6 and x6==1:
    cont2=1
elif x7==x8 and x8==x9 and x9==1:
    cont2=1
elif x1==x4 and x4==x7 and x7==1:
    cont2=1
elif x2==x5 and x5==x8 and x8==1:
    cont2=1
elif x3==x6 and x6==x9 and x9==1:
    cont2=1
elif x1==x5 and x5==x9 and x9==1:
    cont2=1
elif x3==x5 and x5==x7 and x7==1:
    cont2=1
if cont1==1:
    print '0'
elif cont2==1:
    print '1'
else:
    'E'

    
    
    

