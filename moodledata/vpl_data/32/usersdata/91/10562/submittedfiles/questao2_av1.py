# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
x1=int(input('Digite um numero:'))
x2=int(input('Digite um numero:'))
x3=int(input('Digite um numero:'))
x4=int(input('Digite um numero:'))
x5=int(input('Digite um numero:'))
x6=int(input('Digite um numero:'))
y1=int(input('Digite o numero sorteado:'))
y2=int(input('Digite o numero sorteado:'))
y3=int(input('Digite o numero sorteado:'))
y4=int(input('Digite o numero sorteado:'))
y5=int(input('Digite o numero sorteado:'))
y6=int(input('Digite o numero sorteado:'))

cont=0

if x1==y1 or x1==y2 or x1==y3 or x1==y4 or x1==y5 or x1==y6 and x2==y1 or x2==y2 or x2==y3 or x2==y4 or x2==y5 or x2==y6 and x3=y1 or x3==y2 or x3==y3 or x3==y4 or x3==y5 or x3==y6 and x4==y1 or x4==y2 or x4==y3 or x4==y4 or x4==y5 or x4==y6 and x5==y1 or x5==y2 or x5==y3 or x5==y4 or x5==y5 or x5==y6 and x6==y1 or x6==y2 or x6==y3 or x6==y4 or x6==y5 or x6==y6:
    cont=cont+6
    print('sena')
else:
    if x1==y1 or x1==y2 or x1==y3 or x1==y4 or x1==y5 or x1!=y6 or