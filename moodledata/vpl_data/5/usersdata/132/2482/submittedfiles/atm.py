# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a=  int(input('digite a quantia a ser sacada'))
x=a/20
y=(a%20)/10
z=(a%20)%10/5
t=(a%20)%10%5/2
w=(a%20)%10%5%2/1
print('%.d'%x,y,z,t,w)