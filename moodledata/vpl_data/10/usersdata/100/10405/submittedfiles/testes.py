# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
pontos = 0
quest = 1
while quest <=3:
    resp = input('Digite o valor:')
    if quest ==1 and resp == "b":
        pontos = pontos +1
    if quest ==2 and resp == "a":
        pontos = pontos +1
    if quest ==3 and resp == "d":
        pontos =pontos +1
    quest+=1
print pontos
