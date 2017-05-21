# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados:'))
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número'))
cont=0
cm=2
while cont<n:
    if cm%a==0 or cm%b==0:
        print('%d'%cm)
        cont=cont+1
    cm=cm+1