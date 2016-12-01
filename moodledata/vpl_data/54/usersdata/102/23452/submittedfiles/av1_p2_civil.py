# -*- coding: utf-8 -*-
from __future__ import division

a=input('digite a:')
b=input('digite b:')
da=0
db=0
while a>=0:
    da=da+1
    a=a//10
while b>0:
    db=db+1
    b=b//10
    
print('quantidade de digitos de a:%d'%da)
print('quantidade de digitos de b:%d'%db)