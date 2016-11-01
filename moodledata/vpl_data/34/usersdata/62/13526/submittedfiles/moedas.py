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
    elif a%2!=0 and b%2==0:
        qa=0
        qb=c/b
        print qa
        print qb
    else:
        qa=c/a
        qb=0
        print qa
        print qb
        
else:
    print ("N")