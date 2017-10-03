# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a = int(input("Digite o valor que deseja sacar: "))
nv = (a//20)
nd = ((a-(nv*20))//10)
nc= ((a-(nv*20)-(nd*10))//5)
ndd=((a-(nv*20)-(nd*10)-(nc*5))//2)
nu=((a-(nv*20)-(nd*10)-(nc*5)-(ndd*2))//1)
print(nv)
print(nd)
print(nc)
print(ndd)
print(nu)
    
