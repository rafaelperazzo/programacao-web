# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite o valor de um número "a":')
b = input('Digite o valor de um número "b":')
c = input('Digite o valor de um número "c":')

if a>b and a>c:
    print ('O maior número é %d' % a)
elif b>a and b>c:
    print ('O maior núemro é %d' % b)
elif c>a and c>b:
    print ('O maior número é %d' % c)
elif a==b or a==c or b==c:
    print ('Digite números diferentes!')