# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a = int(input('Digite o valor inicial: '))
b = float(input('Digite o valor do juros anual: '))
for i in range(a,a+11,):
    i = i + b
    print('%.2f' %i)