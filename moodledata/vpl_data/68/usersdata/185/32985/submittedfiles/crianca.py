# -*- coding: utf-8 -*-
P1=float(input('digite peso 1:'))
P2=float(input('digite peso 2:'))
C1=float(input('digite comprimento 1:'))
C2=float(input('digite comprimento 2:'))
E=(P1*C1)/(P2*C2)
if E==1:
    print('0')
elif E>1:
    print('-1')
else:
    print ('1')

