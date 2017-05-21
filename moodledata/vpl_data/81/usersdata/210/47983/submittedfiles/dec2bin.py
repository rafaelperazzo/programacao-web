# -*- coding: utf-8 -*-
A=int(input('digite o valor de A:'))
B=int(input('digite o valor de B:'))
cont=0
temp=A
while temp>0:
    cont=cont+1
    temp=temp//10
cont2=0
while (B>0):
    n=B%(10**cont)
    if n==A:
        cont2=cont2+1
    B=B//10
if cont2>0:
    print('S')
else:
    print('N')
    



























