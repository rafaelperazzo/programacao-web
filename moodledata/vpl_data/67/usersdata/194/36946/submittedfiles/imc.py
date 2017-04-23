# -*- coding: utf-8 -*-
x1=input('digite o nome:')
p=float(input('digite seu peso' + x1 + ':'))
h=float(input('digite sua altura' + x1 + ':'))
imc=p/(h**2)
if imc<20:
    print('abaixo')
elif 20<=imc<=25:
    print('normal')
elif 25<imc<=30:
    print('sobrepeso')
elif 30<imc<=40:
    print('obesidade')
elif imc>40:
    print('obesidade grave')
   



