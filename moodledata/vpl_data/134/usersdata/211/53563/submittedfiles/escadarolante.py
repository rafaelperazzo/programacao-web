# -*- coding: utf-8 -*-
A=int(input('escreva a quantidade de pessoas:'))
for i in range(1,A+1,1):
    t=int(input('dite o tempo:'))
    if i==1:
        t1=t
    if i==A:
        t2=t
tempo=t2-t1+10
print(tempo)
        