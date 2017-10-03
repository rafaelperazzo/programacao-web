# -*- coding: utf-8 -*-
x = int(input('Digite um número: '))
if x+90000000 <= 100000000:
    print('NAO SEI')
else:
    n = x%10
    nn = n//10
    print(nn)