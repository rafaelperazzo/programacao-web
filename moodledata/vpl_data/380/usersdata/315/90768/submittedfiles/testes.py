# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random

def par(x):
    if x%2 ==0:
        return x+' e par'
    else:
        return x+' e impar'
        
while True:
    par(int(input('digite valor: ')))


