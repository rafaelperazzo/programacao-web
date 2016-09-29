# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
Q = int(input())

vinte = Q//20
dez = (Q-(vinte*20))//10
cinco = (Q-(vinte*20)-(dez*10))//5
dois = (Q-(vinte*20)-(dez*10)-(cinco*5))//2
um = (Q-(vinte*20)-(dez*10)-(cinco*5)-(dois*2))

print vinte
print dez
print cinco
print dois
print um