# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI

T1= int(input('Entrada da régua1: '))
for T1 in range(T1,0,-1):
    T2= int(input('Entrada da régua2: '))
    for T2 in range(T2,0,-2):
        T3= int(input('Entrada da régua3: '))
        for T3 in range(T3,0,-3):
            T4= int(input('Entrada da régua4: '))
            Tn= (T1-1)+(T2-1)+(T3-1)+T4
            print (Tn)
            break

