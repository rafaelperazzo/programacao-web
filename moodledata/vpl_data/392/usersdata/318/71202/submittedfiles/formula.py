# -*- coding: utf-8 -*-

#ENTRADA
P = float(input('Digite valor para P: '))
i = float(input('Digite valor para i: '))
n = float(input('Digite valor para n: '))

#PROCESSAMENTO
v = P*((((1+i)**n)-1)/i)

#SAIDA
print('%.2f' % v)