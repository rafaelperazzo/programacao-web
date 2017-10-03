# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI
P = int (input('Digite a posicao da porta P: '))
R = int (input('Digite a posicao da porta R: '))

if (P==1) and (R==1):
    print ('A')
elif (P==0) and (R==0):
    print ('C')
elif (P==1) and (R==0):
    print ('B')
elif (P==0) and (R==1):
    print ('C')