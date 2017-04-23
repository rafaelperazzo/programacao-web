# -*- coding: utf-8 -*-
import math

p=int(input('Digite a posição da portinha p: '))
r=int(input('Digite a posição da portinha r: '))
if p==0 and r==0:
    print('C')
if p==0 and r==1:
    print('C')
if p==1 and r==0:
    print('B')
if p==1 and r==1:
    print('A')