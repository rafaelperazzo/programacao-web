# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI

L=input('posição do lançador:')
R=input('posição do recebedor:')
D=input('posição do defensor:')

if(R>50) and (L<R) and (R>D):
    print('S')
    
else:
    print('N')