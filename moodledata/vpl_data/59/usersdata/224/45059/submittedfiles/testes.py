# -*- coding: utf-8 -*-
v=float(input('Digite o valor v: '))
t=float(input('Digite o valor t: '))  
investimento=0
i=1
for i in range(1,11,1):
    investimento=v+(t*v)
    investimento=investimento+1
    print('%.2f'%investimento)