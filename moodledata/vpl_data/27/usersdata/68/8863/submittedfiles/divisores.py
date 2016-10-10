# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input ('Digite a quantidade de números a serem mostrados:')
a=input ('Digite o valor de a:')
b=input ('Digite o valor de b:')
i=2
cont=0

while cont<n:
    if i%a==0 or i%b==0:
        print (i)
        cont=cont+1
    i=i+1
