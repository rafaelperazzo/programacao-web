# -*- coding: utf-8 -*-
p= float(input(' Digite um valor para P:'))
i= float(input('Digite um valor para I:'))
n= float(input('Digite um valor para N:'))

v= ((p*(1+i)**n)-1)/i

print('%.2f' %v)
