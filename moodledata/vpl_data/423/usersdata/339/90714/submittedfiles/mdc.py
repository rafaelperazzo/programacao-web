# -*- coding: utf-8 -*-
import math

def primo(x):
    cont=0
    for i in range (2,x,1):
        if x%i==0:
            cont+=1
            return True
        else:
            cont=0
            return False


primo(int(input('x: ')))
if cont == 0:
    print ('primo')
else:
    print ('bnao')
        



