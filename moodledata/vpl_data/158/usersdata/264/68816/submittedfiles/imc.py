# -*- coding: utf-8 -*-
#Entrada:
peso= float(input('Digite o valor do peso em Kg:'))
altura= float(input('Digite o valor da altura em metros:'))
#Processamento:
imc= ((peso)/(altura**2))
#Saída:
if (imc<20):
    print ('ABAIXO')
if (20<imc<=25):
    print ('NORMAL')
if (25<imc<=30):
    print ('SOBREPESO')
if (30<imc<=40):
    print ('OBESIDADE')
if (imc>40):
    print ('OBESIDADE GRAVE')
