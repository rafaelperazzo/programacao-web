# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
t1= input('numero de tomadas t1:')
t2= input('numero de tomadas t2:')
t3= input('numero de tomadas t3:')
t4= input('numero de tomadas t4:')
#PROCESSAMENTO
totalUm= t1-1
totalDois= t2-1
totalTres= t3-1
nTotal= totalUm + totalDois + totalTres + t4
#SAIDA
print('%d' %nTotal)

