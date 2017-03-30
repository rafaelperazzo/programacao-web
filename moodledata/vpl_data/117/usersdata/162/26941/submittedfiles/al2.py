# -*- coding: utf-8 -*-
a=float(input('Digite um número:'))
b=(a-(a%1))
c=(a%1)
print('O valor inteiro é %d' %b)
print('O valor decimal é %.6f' %c)