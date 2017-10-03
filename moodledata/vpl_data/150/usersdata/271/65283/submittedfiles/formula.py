# -*- coding: utf-8 -*-
#ENTRADA
p = float(input('Digite o valor de p: '))
i = float(input('Digite o valor de i: '))
n = float(input('Digite o valor de n: '))
#PROCESSAMENTO
v = p*(((1+i)**n)-1)/i
#SAÍDA
print('%.2f' % v)