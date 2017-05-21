# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas:'))
cont=1
while cont<=n:
    t=int(input('digite o tempo que a pessoa passou:'))
    if cont==1:
        t1=t
    if cont==n:
        tempo=(t+10)-t1
    cont=cont+1
print(tempo)