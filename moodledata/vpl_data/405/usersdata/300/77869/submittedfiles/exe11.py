# -*- coding: utf-8 -*-
x = int(input('Digite um número: '))
if 100000000 < x+90000000 < 190000000:
    s = 0
    s += x%8
    x //= 8
    print(s)
else:
    print('NAO SEI')