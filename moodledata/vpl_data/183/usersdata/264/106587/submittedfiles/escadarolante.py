# -*- coding: utf-8 -*-
N= int(input('Digite a quantidade de pessoas:'))
T1= int(input('Digite o primeiro tempo:'))

for i in range (0,N-1,1):
    T= int(input('Digite o tempo que as pessoas passaram:'))
    cont= T-T1
    F= cont+T-T+10

print (F)