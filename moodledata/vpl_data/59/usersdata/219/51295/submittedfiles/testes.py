# -*- coding: utf-8 -*-
#COMECE AQUI
a=float(input('Digite o valor do investimento:'))
b=float(input('Digite o valor da taxa:'))
x=0
while x<=10:
    a=a+b*a
    x=x+1
    print('%.2f' %a)


       