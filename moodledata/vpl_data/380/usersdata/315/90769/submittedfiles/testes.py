# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random

def par(x):
    if x%2 ==0:
        return str(x+' e par')
    else:
        return str(x+' e impar')
        
while True:
    par(int(input('digite valor: ')))


