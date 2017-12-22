# -*- coding: utf-8 -*-
import math

n = int(input('informe o numero de multiplos: ' ))
a = int(input( 'informe o numero a: '))
b = int(input('infomre o numero b: ' ))
k = 1

for i in range (0,n-6,1):
    a = a*k
    b = b*k
    print( '%.d' %a)
    print( '%.d' %b)
    k = k + 1

