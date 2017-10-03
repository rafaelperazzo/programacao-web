# -*- coding: utf-8 -*-
peso = float(input('Digite seu peso em kg (quilogramas): '))
altura = float(input('Digite sua altura em m (metros): '))

imc = peso/(altura*altura)

if (imc<20):
    print ('abaixo')
elif (20<=imc) and (imc<=25):
    print ('normal')
elif (25<imc) and (imc<=30):
    print ('sobrepeso')
elif (30<imc) and (imc<=40):
    print ('obesidade')
elif (imc>40):
    print ('obesidade grave')


