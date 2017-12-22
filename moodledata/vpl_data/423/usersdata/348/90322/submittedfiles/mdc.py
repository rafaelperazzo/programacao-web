# -*- coding: utf-8 -*-
import math


n1 = int(input( 'informe o numero 1: ' ))
n2 = int(input(' informe o numero 2: '))

k = n1+n2

while True:
    k = k-1
    if n1%k == 0 and n2%k == 0:
        break
print('%.d' %k)
    






'''
k = 100000 

while True:
    k = k - 1
    if n1%k == 0 and n2%k == 0 :
        break
print('%.d' %k)
'''