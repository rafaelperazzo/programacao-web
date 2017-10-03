# -*- coding: utf-8 -*-
#ENTRADA
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
Delta = (b*b)-(4*a*c)
#PROCESSAMENTO
if Delta>=0 :
    x1 = (-b+(Delta**(1/2)))/(2*a)
    x2 = (-b-(Delta**(1/2)))/(2*a)
    print(x1)
    print(x2)
else :
    print('SRR')

