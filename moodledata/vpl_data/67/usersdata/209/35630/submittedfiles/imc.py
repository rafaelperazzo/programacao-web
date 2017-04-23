# -*- coding: utf-8 -*-
h:float(input('Digite a altura(m):'))
p:float(input('Digite o peso(kg):'))
imc:p/h**2
if imc<20:
    print('ABAIXO')
elif 20<=imc<=25:
    print('NORMAL')
elif 25<imc<=40:
    print('SOBREPESO')
elif 30<imc<=40:
    print('OBESIDADE')
elif imc>40:
    print('OBESIDADE GRAVE')

