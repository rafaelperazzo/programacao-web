# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('digite a:'))
b = int(input('digite b:'))
c = int(input('digite c:'))
d = int(input('digite c:'))

if a==2 or a==3 or a==5 or a==8 or a==9 and b==2 or b==3 or b==5 or b==8 or b==9 and c==2 or c==3 or c==5 or c==8 or c==9 and d==2 or d==3 or d==5 or d==8 or d==9:
    print('V')
elif a==1 or a==4 or a==7 and b==1 or b==4 or b==7 and c==1 or c==4 or c==7 and d==1 or d==4 or d==7:
    print('F')