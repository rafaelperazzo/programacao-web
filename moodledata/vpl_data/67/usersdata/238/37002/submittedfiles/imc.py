# -*- coding: utf-8 -*-
p=float(input('digite seu peso:'))
h=float(input('digite sua altura:'))
imc=p/h**2
if imc<20:
    print('abaixo')
elif 20<=imc<=25:
    print ('normal')
elif 25<=imc<=30:
    print('sobrepeso')
elif 30<=imc<=40:
    print('obesidade grave')
    

