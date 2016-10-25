# -*- coding: utf-8 -*-
from __future__ import division

#entrada
a=int(input('insira o valor de a:')
final=0
pot2=1
while a!=0:
    final=final+a%10*pot2
   a=a/10
   pot2=pot2*2
   print('%d'final)