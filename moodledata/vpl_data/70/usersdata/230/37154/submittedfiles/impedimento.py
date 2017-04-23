# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Digite posição jogador L(lança): '))
R=int(input('Digite posição jogador R(recebe): '))
D=int(input('Digite posição jogador D(defende): '))
if R>50 and L>R and R>D:
    print('S')
else:
    print('N')
