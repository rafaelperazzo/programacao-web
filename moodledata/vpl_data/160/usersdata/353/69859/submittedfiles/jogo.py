# -*- coding: utf-8 -*-
import math
#ENTRADA
Cv=int(input('Valor de Cv: '))
Ce=int(input('Valor de Ce: '))
Cs=int(input('Valor de Cs: '))
Fv=int(input('Valor de Fv: '))
Fe=int(input('Valor de Fe: '))
Fs=int(input('Valor de Fs: '))
#PROCESSAMENTO
a=Cv+Ce
b=Fv+Fe
#SAIDA
if a>b:
    print ('C')
elif a<b:
    print ('F')
elif Cs>Fs:
    print ('C')
elif Cs<Fs:
    print ('F')
else:
    print ('=')
