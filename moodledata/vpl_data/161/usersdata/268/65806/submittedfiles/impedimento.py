# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

L=int(input(' L '))
R=int(input(' R '))
D=int(input(' D '))

if(R>50) and (L>R) and (R>D):
    print('S')
else:
    print('N')