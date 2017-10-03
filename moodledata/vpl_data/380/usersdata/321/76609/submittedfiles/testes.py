# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
va= input('Digite a: ')
vb= input('Digite b: ')
vc= input('Digite c: ')

de= int(vb*vb)
lta= int(4*a*c)
delta= int( de - lta)

if delta<0 :
    print('SRR')
else :
    delta=(b**2)-(4*a*c)
    x1=(-b+delta**1/2)/2*a
    x2=(-b-delta**1/2)/2*a
    print(x1 and x2)