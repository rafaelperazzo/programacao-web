# -*- coding: utf-8 -*-
n=int(input('digite n:'))
cont=1
while cont<=n:
    t=int(input('digite t:'))
    if cont==1:
        t1=t
    if cont==n:
        tempo=(t+10)-t1
    cont=cont+1
print(tempo)