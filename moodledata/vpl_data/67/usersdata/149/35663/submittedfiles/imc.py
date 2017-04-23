# -*- coding: utf-8 -*-
X1=input('digite seu nome:')
p=float(input('Digite seu peso ' + X1 + ':'))
h=float(input('Digite sua altura ' + X1 + ':'))
imc=p/h**2
if imc<20:
    print('abaixo')
if 20<=imc<=25:
    print('normal')
if 25<imc<=30:
    print('sobrepeso')
if 30<imc<=40:
    print('obesidade')
if imc>40:
    print('obesidade grave')

