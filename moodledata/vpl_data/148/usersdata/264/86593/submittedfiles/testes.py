# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
inves= int(input('Digite o valor:'))
taxa= float(input('Digite o valor:'))
cont=0
soma= 0
while cont<=10:
    soma= inves+(inves*taxa)
    cont= cont+1
    print ('%.2f' %soma)
    inves=soma