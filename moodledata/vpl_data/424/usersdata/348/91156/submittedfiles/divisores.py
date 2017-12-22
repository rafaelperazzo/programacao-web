# -*- coding: utf-8 -*-
import math

n = int(input('informe o numero de multiplos: ' ))
a = int(input( 'informe o numero a: '))
b = int(input('infomre o numero b: ' ))
k = 0

for i in range (0,n-3,1):
    k = k + 1
    j = a*k
    l = b*k
    print('%.d' %j)
    print('%.d' %l)
    

