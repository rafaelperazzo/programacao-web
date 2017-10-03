# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
R = float (input('Digite o valor de R: '))
L = float (input('Digite o valor de L: '))
D = float (input('Digite o valor de D: '))

if (R>50) and (L<R) and (R>D):
    print ('S')
else:
    print ('N')