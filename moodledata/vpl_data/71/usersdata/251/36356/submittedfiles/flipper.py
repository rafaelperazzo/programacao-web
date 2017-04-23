# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO AQUI
p = int(input ('Digite 0 ou 1 para a posição de esquerda ou direita, respectivamente, da porta P: '))
r = int(input ('Digite 0 ou 1 para a posição de esquerda ou direita, respectivamente, da porta R: '))

if p==1 and r==1:
    print('A')
    
elif p==1 and r==0:
    print('B')
    
elif p==0:
    print('C')