# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
i=1
#PROCESSAMENTO/SAIDA
if c%a==0 or c%b==0:
    qa=c//a
    qb=(c%a)//b
    print qa
    print qb
else:
    print N