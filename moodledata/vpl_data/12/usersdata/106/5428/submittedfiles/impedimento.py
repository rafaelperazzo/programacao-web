# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI
L = input ('Diga qual a posição do jogagor L:')
R = input ('Diga qual a posição do jogador R:')
D = input ('Diga qual a posição do jogador D:')

#processamento
if R>50 and L<R and R>D:
    print ('S')
else:
    print ('N')