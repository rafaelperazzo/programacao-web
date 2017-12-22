# -*- coding: utf-8 -*-
import math

n = int(input('informe o numero de multiplos: ' ))
a = int(input( 'informe o numero a: '))
b = int(input('infomre o numero b: ' ))
k = 1

for i in range (0,n,1):
    k = k + 1
    if k%a == 0:
        print('%.d' %k)
    if k%b ==0:
        print('%.d' %k)
    

