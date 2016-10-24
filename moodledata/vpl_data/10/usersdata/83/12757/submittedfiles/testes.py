# -*- coding: utf-8 -*-
from __future__ import division

n=5
i=1
j=0
maior=j
while i<=n :
    k=input('Digite o valor de venda do dia %d: ' %i)
    if k>=maior :
        maior=k
        d=i
    i=i+1
print ('%d maior quantidade de vendas e %d do mês de abril' %(maior,d))