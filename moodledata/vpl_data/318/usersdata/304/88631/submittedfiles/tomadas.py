# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
t1 = int(input('T1: '))
while not int(t1)>1.0:
    int(input('T1: '))
t2 = int(input('T2: '))
while not int(t2)>1.0:
    int(input('T2: '))
t3 = int(input('T3: '))
while not int(t3)>1.0:
    int(input('T3: '))
t4 = int(input('T4: '))
while not int(t4)>1.0:
    int(input('T4: '))

tn = ((t1-1)+(t2-1)+(t3-1)+t4)
print(tn)