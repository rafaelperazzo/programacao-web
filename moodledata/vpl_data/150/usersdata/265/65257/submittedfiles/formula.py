# -*- coding: utf-8 -*-
#ENTRADA
p = float(input('digite o valor de P: '))
i = float(input('digite o valor de i: '))
n = float(input('digite o valor de n: '))
#PROCESSAMENTO
v=p*((((1+i)**n)-1)/i)
#SAÍDA
print('%.2f' %v)