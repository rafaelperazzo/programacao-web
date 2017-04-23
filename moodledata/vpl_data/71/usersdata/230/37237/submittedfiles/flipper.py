# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI
P=int(input('Digite posição portinha de P: '))
R=int(input('Digite posição portinha de R: '))
if P==1 and R==1:
    print('A')
elif P==1 and R==0:
    print('B')
else:
    print('C')