# -*- coding: utf-8 -*-
v=float(input('Digite o valor v: '))
t=float(input('Digite o valor t: '))  
for i in range(1,11,1):
    investimento=v+(t*v)
    investimento=investimento+(t*v)
    print('%.2f'%investimento)