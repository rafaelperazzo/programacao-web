# -*- coding: utf-8 -*-

p=float(input('digite o peso(kg):'))
a=float(input('digite a altura(m):'))
imc=(p/(a**2))
if(imc<20):
    print('ABAIXO')
elif(imc>20)and(imc<=25):
    print('NORMAL')
elif(imc>25)and(imc<=30):
    print('SOBREPESO')
elif(imc>30)and(imc<=40):
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
    
