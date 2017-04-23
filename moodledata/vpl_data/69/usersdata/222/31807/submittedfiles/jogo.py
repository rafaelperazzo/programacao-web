# -*- coding: utf-8 -*-
import math
Cv=int(input(' Digite Cv: '))
Ce=int(input(' Digite Ce: '))
Cs=int(input(' Digite Cs: '))
Fv=int(input(' Digite Fv: '))
Fe=int(input(' Digite Fe: '))
Fs=int(input(' Digite Fs: '))
PC= Cv*3 + Ce*1
PF= Fv*3 + Fe*1
if PC > PF:
    print('C')
elif PF > PC:
    print('F')
elif Cs > Fs:
    print('C')
elif Fs > Cs:
    print('F')
elif Fs=Cs:
    print('=')


    
