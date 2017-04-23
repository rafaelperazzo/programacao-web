# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI
P=int(input('Digite P: '))
R=int(input('Digite R: '))
if (P==0) or (P==1) and (R==0) and (R==1):
    if (P==0):
        if (R==0):
            print('A')
        else:
            print('B')
    else:
        print('C')