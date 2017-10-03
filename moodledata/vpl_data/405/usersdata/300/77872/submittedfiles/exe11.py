# -*- coding: utf-8 -*-
x = int(input('Digite um número: '))
if 100000000 < x+90000000 < 190000000:
   n = x//80000000
   m = n -(x%8)
   print(m)
else:
    print('NAO SEI')