# -*- coding: utf-8 -*-
from __future__ import division

#Calcula o número de vidas ao sair da sala.
def conta_vida(p,pe,ps):    #p = porta; pe = porta de entrada; ps = porta de saida.
    s = 0
    for i in range(pe, ps + 1, 1):
       s = s + p[i]
    return s

p = input('Quantidade de salas:')
a = []
print('Preencha a quantidade de vidas para cada sala.')
for i in range(0, p, 1):
    print ('Porta %d' %i)
    a.append(input('Número de vidas:'))
pe = input('Porta de entrada:')
ps = input('Porta de saida:')
if pe<ps:
    print ('O número de vidas obtidas é:%d' %conta_vida(a,pe,ps))
else:
    print ('O número de vidas obtidas é:%d' %conta_vida(a,ps,pe))

