# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input('Valor do saque:'))
if valor>=20:
    ced20=valor/20
rced20=valor%20
if rced20>=10:
    ced10=rced20/10
rced10=ced20%10
ced5=rced10/5
print(int(ced20))
print(int(ced10))
print(int(ced5))


