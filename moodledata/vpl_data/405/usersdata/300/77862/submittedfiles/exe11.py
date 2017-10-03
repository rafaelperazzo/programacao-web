# -*- coding: utf-8 -*-
x = int(input('Digite um número: '))
if 190000000 < x+90000000 < 100000000:
    print('NAO SEI')
else:
    n = x%8
    nn = n//10
    print(nn)