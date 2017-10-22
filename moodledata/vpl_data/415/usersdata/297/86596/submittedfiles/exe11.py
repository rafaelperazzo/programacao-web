# -*- coding: utf-8 -*-
x=int(input("digite um numero de 8 algarismos: "))
m=100000000
soma=0
if 10000000>=x<100000000 :
    while soma<72 or x<0 :
        m=m/10
        a=x//m
        x=x%m
        soma=soma+a
    print('%d'%soma)
else :
    print('NAO SEI')