# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
inves= int(input('Digite o valor:'))
taxa= int(input('Digite o valor:'))
soma=0
for i in range (0,10,1):
    soma= soma+(inves*taxa)
    print ('%.2f' %soma)
soma= soma