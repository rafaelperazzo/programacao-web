# -*- coding: utf-8 -*-
import math
Cv=int(input('Digite um número:'))
Ce=int(input('Digite um número:'))
Cs=int(input('Digite um número:'))
Fv=int(input('Digite um número:'))
Fe=int(input('Digite um número:'))
Fs=int(input('Digite um número:'))
a=Cv*3+Ce
b=Fv*3+Fe
if a>b:
    print('C')
else:
    print('F')
    if a==b:
        if Cs>Fs:
            print('C')
        else:
            print('F')
