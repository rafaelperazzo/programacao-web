# -*- coding: utf-8 -*-
import math
a=float(input('digite a: '))
b=float(input('digite b: '))
c=float(input('digite c: '))
d=float(input('digite d: '))
decisao=0

if a>b:
    decisao=decisao+1
    
if b>a and b>c:
    decisao=decisao+1
    
if c>b and c>d:
decisao= decisao+1

if d>c:
    decisao=decisao+1
    
if decisao==1:
    print('S')
else:
    print('N')