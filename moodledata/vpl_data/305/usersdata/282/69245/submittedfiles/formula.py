# -*- coding: utf-8 -*-
print('Boa tarde, seja bem vindo')
print('\n'-------------------------------------------------------)
P = float(input('Digite P: ')) 
i = float(input('Digite i: '))
n = float(input('Digite n: '))
V = P*((((1+i)**n)-1)/i)
print('O valor de V eh %.2f' %V)
