# -*- coding: utf-8 -*-
q=int(input('Digite a quatidade de pessoas: '))
soma=0
for i in range (0,q,1):
    idade=int(input('Digite a idade de cada pessoa: '))
    soma=soma+idade
media=soma/q
print (media)
