# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite n:')
a=input('Digite a:')
b=input('Digite b:')
cont=1
i=1
#PROCESSAMENTO
while cont<=n:
    if i%a==0 or i%b==0 :
        print i
        cont = cont+1
    i = i+1
