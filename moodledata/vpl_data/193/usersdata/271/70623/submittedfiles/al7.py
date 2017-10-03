# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite o valor de n : '))
i = 1
div = 0
#PROCESSAMENTO
while (i<=(n/2)) :
    div = div+(n//i)
    i = i+1
if (div==n) :
    print('PERFEITO')
if (div!=n) :
    print('NÃO PERFEITO')

