# -*- coding: utf-8 -*-
#Entrada:
a= float(input('Digite o valor de a:'))
b= float(input('Digite o valor de b:'))
c= float(input('Digite o valor de c:'))
#Processamento:
delta= (b*b)-4*a*c
if (delta<0):
    print('Não existem raíes reais para a equação.')
if (delta>=0):
    x1=(-b+(delta**(1/2)))/(2*a)
    x2=(-b-(delta**(1/2)))/(2*a)
    print(x1)
    print(x2)