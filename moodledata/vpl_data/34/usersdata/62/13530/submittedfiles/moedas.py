# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
#PROCESSAMENTO/SAIDA
if c%a==0 or c%b==0:
    if a%2==0 and b%2==0:
        qa=c//a
        qb=(c%a)//b
        print qa
        print qb
    if a%2!=0 and b%2==0 and c%2==0:
        qa=0
        qb=c/b
        print qa
        print ("%.d"%qb)
    if a%2==0 and b%2!=0 and c%2==0:
        qa=c/a
        qb=0
        print ("%.d"%qa)
        print qb
    if c%2!=0 and c%a==0:
        qa=c/a
        qb=0
        print ("%.d"%qa)
        print qb
    if c%2!=0 and c%b==0:
        qa=0
        qb=c/b
        print ("%.d"%qb)
        print qa
else:
    print ("N")