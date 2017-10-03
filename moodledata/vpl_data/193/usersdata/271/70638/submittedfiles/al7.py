# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite o valor de n : '))
i = 1
divi = 0
#PROCESSAMENTO
while (i<n) :
    if (n%i==0) :
        divi = (divi+i)
        i=i+1
if (divi==n) :
    print('PERFEITO')
if (divi!=n) :
    print('NÃO PERFEITO')


