# -*- coding: utf-8 -*-
N=int(input('Digite o número de pessoas:'))
cont=1
while cont<=N:
    T=float(input('Digite o tempo que a pessoa passou:'))
    if cont==1:
        T1=T
    if cont==N:
        TEMPO=(T+10)-T1
    cont=cont+1
print(TEMPO)
    