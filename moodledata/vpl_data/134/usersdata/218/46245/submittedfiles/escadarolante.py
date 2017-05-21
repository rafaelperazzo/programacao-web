# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de pessoas:'))
T=0
nf=0
for i in range (0,n,1):
    t=int(input('tempo:'))
    if i==0:
        t1=t
    if i==n:
        nf=t+10
T=nf-t1
print(T)