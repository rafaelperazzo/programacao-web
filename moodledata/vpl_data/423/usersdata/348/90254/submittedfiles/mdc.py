# -*- coding: utf-8 -*-
import math


n1 = int(input( 'informe o numero 1: ' ))
n2 = int(input(' informe o numero 2: '))

k = 1000000000000 

while True:
    if n1%k == 0 and n2%k == 0 :
        break
    k=k -1
print('%.d' %k)