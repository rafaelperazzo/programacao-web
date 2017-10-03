# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
l= int(input('Digite a posição do jogador l (entre 0 e 100 metros):'))
r= int(input('Digite a posição do jogador r (entre 0 e 100 metros):'))
d= int(input('Digite a posição do jogador d (entre 0 e 100 metros):'))
#Processamento e Saída:
if (r>50) and (l<r) and (r>d):
    print ('S')