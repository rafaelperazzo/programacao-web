# -*- coding: utf-8 -*-
n=int(input('digite um numero inteiro maior que um:'))
ant=int(input('digite um numero:'))
ma=0
i=1
while i<n:
    atu=int(input('digite um numero:'))
    i=i+1
    ad=atu-ant
    if ad<0:
        ad=-ad
    elif ad>ma:
        ma=md
    else:
        ant=atu
print(ma)

