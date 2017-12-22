# -*- coding: utf-8 -*-

v=int(input('Volume inicial: '))
t=int(input('Número de modificacoes: '))
for i in range(0,t,1):
    m=int(input('Modificacao: '))
    v=(v+m)
    if(v>100):
        v=100
    if(v<0):
        v=0
print(v)