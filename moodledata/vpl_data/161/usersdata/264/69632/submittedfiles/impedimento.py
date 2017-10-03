# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L= int(input('Digite a posição do jogador l (entre 0 e 100 metros):'))
R= int(input('Digite a posição do jogador r (entre 0 e 100 metros):'))
D= int(input('Digite a posição do jogador d (entre 0 e 100 metros):'))
#Processamento e Saída:
if (R>50) and (L<R) and (R>D):
    print("S")
else:
    ("N")