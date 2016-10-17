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

if x1==y1 and x2==y2 and x3==y3 and x4==y4 and x5==y5 and x6==y6:
    cont=cont+6
    print('sena')
    else:
        if x1==y1 and x2==y2 and x3==y3 and x4==y4 and x5==y5 and x6!=y6:
            cont=cont+5
            print('quina')
else:
    if x1==y1 and x2==y2 and x3==y3 and x4==y4 and x5!=y5 and x6!=y6:
        cont=cont+4
        print('quadra')
else:
    if x1==y1 and x2==y2 and x3==y3 and x4!=y4 and x5!=y5 and x6!=y6:
        cont=cont+3
        print('terno')
else:
    print('azar')