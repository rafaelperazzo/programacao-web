# -*- coding: utf-8 -*-
from __future__ import division
a= float(input('Digite valor de a da função: '))
b= float(input('Digite o valor de b da função: '))
c= float(input('Digite o valor de c da função: '))
Delta= (b**2)-(4*a*c)
x1=(-b+(Delta**(1/2)))/2
x2=(-b-(Delta**(1/2)))/2
if Delta < 0:
    print ('A equação não possui raizes reais.')
elif Delta == O:
    print ('A equação possui duas raizes iguais'%x1)
else :
    print ('A raiz possui duas raizes: %.f /n %.f'%(x1,x2))
    