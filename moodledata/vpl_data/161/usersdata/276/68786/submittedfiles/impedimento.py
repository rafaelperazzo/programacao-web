# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
R = int (input('Digite o valor de R: '))
L = int (input('Digite o valor de L: '))
D = int (input('Digite o valor de D: '))

if (R>50) and (L<R) and (R>D):
    print ('S')
else:
    print ('N')