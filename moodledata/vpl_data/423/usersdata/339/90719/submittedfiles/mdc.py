# -*- coding: utf-8 -*-
import math

def primo(x):
    cont=0
    for i in range (2,x,1):
        if x%i==0:
            cont+=1
            return 'nao'
        else:
            cont-=1
            return 'prim0o'


print (primo(int(input('x: '))))

        



