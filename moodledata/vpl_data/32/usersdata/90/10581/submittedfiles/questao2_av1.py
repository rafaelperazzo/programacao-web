# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

a=int(input('Digite aqui o 1 numero apostado por Yoko:'))
b=int(input('Digite aqui o 2 numero apostado por Yoko:'))
c=int(input('Digite aqui o 3 numero apostado por Yoko:'))
d=int(input('Digite aqui o 4 numero apostado por Yoko:'))
e=int(input('Digite aqui o 5 numero apostado por Yoko:'))
f=int(input('Digite aqui o 6 numero apostado por Yoko:'))

a1=int(input('Digite aqui o 1 numero sorteado:'))
a2=int(input('Digite aqui o 2 numero sorteado:'))
a3=int(input('Digite aqui o 3 numero sorteado:'))
a4=int(input('Digite aqui o 4 numero sorteado:'))
a5=int(input('Digite aqui o 5 numero sorteado:'))
a6=int(input('Digite aqui o 6 numero sorteado:'))

cont=0

if a==a1 or b==a2 or c==a3 or d==a4 or e==a5 or f==a6:
    cont==cont+1
if a==a1 or b==a2 or c==a3 or d==a4 or e==a6 or f==a6:
    cont==cont+1
if a==a1 or b==a2 or c==a3 or d==a6 or e==a6 or f==a6:
    cont==cont+1
if a==a1 or b==a2 or c==a6 or d==a4 or e==a5 or f==a6:
    cont==cont+1
if a==a1 or b==a6 or c==a6 or d==a6 or e==a6 or f==a6:
    cont==cont+1
if a==a6 or b==a6 or c==a6 or d==a6 or e==a6 or f==a6:
    cont==cont+1

if cont==3:
    print('terno')
elif cont==4:
    print('terno')
elif cont==5:
    print('terno')
elif cont==6:
    print('sena')





