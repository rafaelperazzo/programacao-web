# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI
p=int(input('Digite a posição da portinha P: '))
r=int(input('Digite a posição da portinha R: '))
if(p==0):
    print('C')
if(p==1)and(r==0):
    print('B')
if(p==1)and(r==1):
    print('A')