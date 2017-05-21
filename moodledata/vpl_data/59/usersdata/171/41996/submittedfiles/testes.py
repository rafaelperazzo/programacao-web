# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
aux=n
dig= reverso =0
while aux !=0:
    dig=aux%10
    reverso=(reverso*10)+dig
    aux=aux//10
if reverso==n:
    print('é palidrome')
else:
    print('não e palidrome')