# -*- coding: utf-8 -*-
pessoas=int(input('Digite o numero de pessoas que passa pela esada rolante:'))
for i in range(1,pessoas+1,1):
    tempo=int(input('Digite o tempo:'))
    if i==1:
        tempo1=tempo
    elif i==pessoas:
        f=tempo+10
x=f-tempo1
print(x)