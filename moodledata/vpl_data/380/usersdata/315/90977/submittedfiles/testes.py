# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random

p = int(input('digite p: '))
q = int(input('digite q: '))
pot10 = 1

while pot10 <=p:
    pot10 = pot10*10
    achou = False
    qaux = q
    while qaux>=p and achou== False:
        subnumero = qaux%pot10
        qaux = qaux/10
        if subnumero==p:
            achou = True
    if achou==True:
        print('S')
    else:
        print('N')





