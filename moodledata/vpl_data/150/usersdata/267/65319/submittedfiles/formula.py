# -*- coding: utf-8 -*-
#ENTRADA
P = float(input('Insira o valor de P: '))
i = float(input('Insira o valor de i: '))
n = float(input('insira o valor de n: '))
#PROCESSAMENTO
v = float(P*((((1+i)**n)-1)/i))
#SAÍDA
print('%.2f' %v)