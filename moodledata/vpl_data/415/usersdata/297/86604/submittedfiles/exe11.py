# -*- coding: utf-8 -*-
x=int(input("digite um numero de 8 algarismos: "))
m=100000000
soma=0
if x>10000000 and x<99999999 :
    for i in range (0,8,1) :
        m= m//10
        a= x//m
        soma=soma+a
        x= x%m
    print('%d'%soma)
else :
    print('NAO SEI')