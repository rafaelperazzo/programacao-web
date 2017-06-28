# -*- coding: utf-8 -*-
import math
def feliz(a):
    soma=0
    for i in range(0,len(a),1):

n=int(input('Digite valor: '))
a=feliz(n)
if feliz(a):
    print('Feliz')
else:
    print('Nao Feliz')