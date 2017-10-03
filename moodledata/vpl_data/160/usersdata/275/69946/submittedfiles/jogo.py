# -*- coding: utf-8 -*-
import math
cv= float(input('Digite o valor: '))
ce= float(input('Digite o valor: '))
cs= float(input('Digite o valor: '))
fv= float(input('Digite o valor: '))
fe= float(input('Digite o valor: '))
fs= float(input('Digite o valor: '))
if cv*3+ce>fv*3+fe:
    print('C')
if cv*3+ce<fv*3+fe:
    print('F')
if cv==fv:
    if ce==fe:
        if cs>fs:
            print('C')
if cv==fv:
    if ce==fe:
        if cs<fs:
            print('F')
            