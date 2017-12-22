# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random

def par(x):
    if x%2 ==0:
        return print('%d e par'%x)
    else:
        return print('%d e impar'%x)
        
while True:
    par(int(input('digite valor: ')))
    print('')

