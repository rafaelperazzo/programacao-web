# -*- coding: utf-8 -*-
import math
cv = float (input('Digite o numero de vitorias do cormengo: '))
ce = float (input('Digite o numero de empates do cormengo: '))
cs = float (input('Digite o saldo de gols do cormengo: '))
fv = float (input('Digite o numero de vitorias do flaminthians: '))
fe = float (input('Digite o numero de empates do flaminthians: '))
fs = float (input('Digite o saldo de gols do flaminthians: '))

pontosc = (cv*3) + (ce*3)
pontosf = (fv*3) + (fe*3)

if (pontosc > pontosf): 
    print ('c')

elif (pontosc < pontosf):
    print ('f')

elif (pontosc == pontosf):
    if (cs>fs):
        print ('c')
    elif (cs<fs):
        print ('f')
    elif (cs==fs):
        print ('=')
        
    