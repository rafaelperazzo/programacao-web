# -*- coding: utf-8 -*-
P=float(input('Digite o valor de P:'))
i=float(input('Digite o valor de i:'))
n=float(input('Digite o valor de n:'))
V=P*((((1+i)**n)-1)/i)
print('O valor de V é: %.2f' % V)