# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n1=input('digite o valor de n1:')
n2=input('digite o valor n2:')
n3=input('dgite o valor n3:')
n4=input('digite o valor n4:')
n5=input('digite o valor n5:')
n6=input('digite o valor n6:')
cont=0
i=1
n=6
while n>=i:
    n5=input('numero sorteado:')
    if n5==n1:
        cont=cont+1
    if n5==n2:
        cont=cont+1
    if n5==n3:
        cont=cont+1
    if n5==n4:
        cont=cont+1
    if n5==n5:
        cont=cont+1
    if n5== n6:
        cont=cont+1
    i=i+1
if cont==3:
    print('terno')
elif cont==4:
    print('quadra')
elif cont==5:
    print('quina')
elif cont ==6:
    print('sena')
else:
    print('azar')
