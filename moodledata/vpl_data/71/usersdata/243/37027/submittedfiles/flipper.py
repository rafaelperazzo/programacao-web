# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI
P=int(input('dig o posiçao da porta 1:'))
R=int(input('dig a posiçao da porta 2:'))

if P==1 and R==0:
    print('B')
elif P==0 and R==1:
    print('B')
elif P==0 and R==0:
    print('C')
elif P==1 and R==1:
    print('A')
else:
    print('A')