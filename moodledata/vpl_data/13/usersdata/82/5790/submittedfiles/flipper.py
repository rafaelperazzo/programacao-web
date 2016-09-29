# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
P= input ('Digite o valor de P:') 
R= input ('Digite o valor de R:') 

#PROCESSAMENTO E SAIDA
if P==0 and R==1:
    print ('C')
else:
    if P==0 and R==0:
        print ('C')
    else:
        if P==1 and R==0:
            print ('B')
        else:
            if P==1 and R==1:
                print ('A')