# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite o valor de n : '))
i = 1
divi = 0
#PROCESSAMENTO
while (i<=(n/2)) :
    if (n%i==0) :
    divi = (divi+i)
    i = i+1
if (div==n) :
    print('PERFEITO')
if (div!=n) :
    print('NÃO PERFEITO')

