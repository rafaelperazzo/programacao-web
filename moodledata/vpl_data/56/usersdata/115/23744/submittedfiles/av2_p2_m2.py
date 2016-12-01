# -*- coding: utf-8 -*-
from __future__ import division

def contagem_vidas(p,pe,ps):
#p=porta, pe=porta em que entrou, ps=porta em que saiu
    s=0
    for i in range(pe,ps+1,1):
        s=s+p[i]
    return s
p=input('Digite a quantidade de salas:')
pe=input('digite a porta escolhida para a entrada')
ps=input('digite a porta escolhida para a saida')
x=[]
for i in range(0,p,1):
    print('porta %d' %(i+1))
    x.append(input('quantidade de vidas:'))
print ('A quantidade de vidas obtidas é:%d' %contagem_vidas(x,pe,ps))