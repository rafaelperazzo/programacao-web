# -*- coding: utf-8 -*-
P = float(input('Digite valor de P: '))
i = float(input('Digite valor de i: '))
n = float(input('Digite valor de n: '))
v = P * (((1+i)**n)-1)/i
print ('%.2f' % v)