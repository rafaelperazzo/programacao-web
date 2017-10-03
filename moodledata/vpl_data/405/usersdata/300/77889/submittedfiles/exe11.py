# -*- coding: utf-8 -*-
x = int(input('Digite um número: '))
if 100000000 < x+90000000 < 190000000:
    a = 0
    b = x%10
    c = (x-b)//10
    a = a + b
    print(a)
else:
    print('NAO SEI')