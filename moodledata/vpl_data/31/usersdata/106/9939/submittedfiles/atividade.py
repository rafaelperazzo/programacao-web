# -*- coding: utf-8 -*-
from __future__ import division
import math

n =  input ('Digite a quantidade de pontos:')
i = 1
while i <=n:
    x= input ('Digite o valor de x:')
    y = input ('Digite o valor de y:')
    if x>=0 and y>=0 and (x**2)+(y**2)<=1:
        print ('Sim')
    else:
        print ('Não')
    i = i+1