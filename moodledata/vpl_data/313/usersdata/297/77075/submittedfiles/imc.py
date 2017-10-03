# -*- coding: utf-8 -*-
peso= float(input('digite seu peso em quilogramas: '))
altura= float(input('digite sua altura em metros: '))
imc = (peso/((altura)^(2)))
if imc<20.0 :
    print('ABAIXO')
elif 20.0<=imc<=25.0 :
    print('NORMAL')
elif 25.0<imc<=30.0 :
    print('SOBREPESO')
elif 30.0<imc<=40.0 :
    print('OBESIDADE')
else :
    print('OBESIDADE GRAVE')
