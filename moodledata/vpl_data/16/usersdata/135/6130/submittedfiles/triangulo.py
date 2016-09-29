# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input ('digite o valor de a: ')
b= input ('digite o valor de b: ')
c= input ('digite o valor de c: ')

if a**2==((b**2)+(c**2)) or a**2>((b**2)+c**2) or a**2< ((b**2)+(c**2)):
    print 'S'
else:
    print 'N'

if a**2==((b**2)+(c**2)):
    print 'Re'

elif  a**2>((b**2)+c**2):
    print 'Ob'

else:
    print 'Ac' 

if a==b==c:
    print 'Eq'

elif b==c!=a:
    print 'Is'

else:
    'Es'
        
