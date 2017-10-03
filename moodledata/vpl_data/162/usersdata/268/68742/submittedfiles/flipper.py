# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI

P=int(input('Digite P'))
R=int(input('Digite R'))
 
if (P==0) and (R==0):
     print('C')
if (P==1) and (R==0):
    print('B')
if (P==1) and (R==1):
    print('A')
if (P==0) and (R==1):
    print('C')