# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada

P= input ('Digite a posição de P:')
R= input ('Digite a posição de R:')

#Processamento e Saida:

if (P==R) and (R==1):
    print ('A')
if (P>R):
    print ('B')
if (P<R) or ((P==R) and (R==0)):
    print ('C') 
