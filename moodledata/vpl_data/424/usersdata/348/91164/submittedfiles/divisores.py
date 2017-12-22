# -*- coding: utf-8 -*-
import math

n = int(input('informe o numero de multiplos: ' ))
a = int(input( 'informe o numero a: '))
b = int(input('infomre o numero b: ' ))
k = 1

for i in range (0,n+2,1):
    k = k + 1
    if k%a == 0 and k%b == 0 or k%a == 0 or k%b == 0:
        print('%.d' %k)

