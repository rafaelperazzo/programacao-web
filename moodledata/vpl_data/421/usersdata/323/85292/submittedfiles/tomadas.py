# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI

T1= int(input('Número de tomadas da tomada 1: '))
T2= int(input('Número de tomadas da tomada 2: '))
T3= int(input('Número de tomadas da tomada 3: '))
T4= int(input('Número de tomadas da tomada 4: '))
while T1>1 and T2>1 and T3>1 and T4>1:
    Total=(T1-1)+(T2-1)+(T3-1)+T4
    print(Total)
    if T1<=1 or T2<=1 or T3<=1 or T4<=1:
        T1= int(input('Número de tomadas da tomada 1: '))
        T2= int(input('Número de tomadas da tomada 2: '))
        T3= int(input('Número de tomadas da tomada 3: '))
        T4= int(input('Número de tomadas da tomada 4: '))