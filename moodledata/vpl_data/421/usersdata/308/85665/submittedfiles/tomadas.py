# -*- coding: utf-8 -*-
import math
def pedirnumero(tomada):
    a = int(input('informe o valor de T%d' % tomada))
    while a<2:
        a = int(input('informe o valor de T%d' % tomada))
    return a

t1 = pedirnumero(1)
t2 = pedirnumero(2)
t3 = pedirnumero(3)
t4 = pedirnumero(4)

print(t1+t2+t3+t4-4)
#COMECE SEU CODIGO AQUI

