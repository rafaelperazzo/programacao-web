# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
inves= int(input('Digite o valor:'))
taxa= float(input('Digite o valor:'))
soma=0
t= inves
for i in range (0,10,1):
    soma= t+(t*taxa)
    t=soma
    print ('%.2f' %soma)
    