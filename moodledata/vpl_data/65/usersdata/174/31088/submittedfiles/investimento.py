# -*- coding: utf-8 -*-
from __future__ import division

i = float(input('Investimento:'))
t = float(input('Taxa percentual:'))
p = t/100
s1 = i+p*i
s2 = s1+p*s1
s3 = s2+p*s2
s4 = s3+p*s3
s5 = s4+p*s4
s6 = s5+p*s5
s7 = s6+p*s6
s8 = s7+p*s7
s9 = s8+p*s8
s10 = s9+p*s9
print('%.2f'%s1)
print('%.2f'%s2)
print('%.2f'%s3)
print('%.2f'%s4)
print('%.2f'%s5)
print('%.2f'%s6)
print('%.2f'%s7)
print('%.2f'%s8)
print('%.2f'%s9)
print('%.2f'%s10)