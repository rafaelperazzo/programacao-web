# -*- coding: utf-8 -*-
x=float(input("digite um numero de 8 algarismos: "))
m=100000000
soma=0
if x>10000000 and x<99999999 :
    while soma<72 or x<0 :
        m= m//10
        a= x//m
        soma=soma+a
        x= x%m
    print('%.0f'%soma)
else :
    print('NAO SEI')