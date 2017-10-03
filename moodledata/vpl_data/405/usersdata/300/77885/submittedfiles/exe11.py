# -*- coding: utf-8 -*-
x = int(input('Digite um número: '))
if 100000000 < x+90000000 < 190000000:
    n = x//10000000
    m = x%10000000
    print(n)
else:
    print('NAO SEI')