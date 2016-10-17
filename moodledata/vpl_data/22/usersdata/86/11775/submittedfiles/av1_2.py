# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('digite a:'))
b = int(input('digite b:'))
c = int(input('digite c:'))
d = int(input('digite c:'))

while a>9 and a==0:
    a = int(input('digite a:'))
while b>9 and b==0:
    b = int(input('digite b:'))
while c>9 and c==0:
    c = int(input('digite c:'))
while d>9 and d==0:
    d = int(input('digite d:'))
    
if a==1 or a==2 or a==3 or a==5 or a==8 or a==9 and b==1 or b==2 or b==3 or b==5 or b==8 or b==9 and c==1 or c==2 or c==3 or c==5 or c==8 or c==9 and d==1 or d==2 or d==3 or d==5 or d==8 or d==9:
    print('V')
else:
    print('F')