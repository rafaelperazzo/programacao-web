# -*- coding: utf-8 -*-
import math
print('Cormengo')
cv=int(input('Número de vitórias: '))
ce=int(input('Número de empates: '))
cs=int(input('Saldo de gols: '))

print ('Flaminthians')
fv=int(input('Número de vitórias: '))
fe=int(input('Número de empates: '))
fs=int(input('Saldo de gols: '))

cpontos= cv*3
fpontos= fv*3

if (cpontos>fpontos):
    print('C')
elif (cpontos<fpontos):
    print('F')
elif (cpontos==fpontos):
    if(ce>fe):
        print('C')
    elif (ce==fe):
        if (cs>fs):
            print ('C')
        elif (cs<fs):
            print('F')
        else:
            print('=')
    else:
        print('F')