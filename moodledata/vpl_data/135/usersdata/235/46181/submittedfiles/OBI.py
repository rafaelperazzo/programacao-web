# -*- coding: utf-8 -*-
n=int(input('digite o numero de participantes:'))
p=int(input('digite o numero de corte:'))
cont=0
for i in range (1,n+1,1):
    x=int(input('digite a nota da fase 1:'))
    y=int(input('digite a nota da fase 2:'))
    if x+y>=p:
        cont=cont+1
print(cont)
