# -*- coding: utf-8 -*-
n=int(input('Digite o número de seções da piscina: '))
while n<=1 or n>=10**5:
    print('Esse número é inválido!')
    n=int(input('Digite o número de seções da piscina: '))
    
    