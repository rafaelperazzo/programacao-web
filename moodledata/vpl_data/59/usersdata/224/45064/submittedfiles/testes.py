# -*- coding: utf-8 -*-
iv=float(input('Digite o valor iv: '))
t=float(input('Digite o valor t: '))  
i=0
for i in range(1,11,1):
    investimento=iv+(t*iv)
    investimento=investimento+(t*iv)
    i=i+1
    print('%.2f'%investimento)