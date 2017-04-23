# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Informe a posição L: '))
R=int(input('Informe a posição R: '))
D=int(input('Informe a posição D: '))

if R>50 and L<R and R>D:
    print('S')
else:
    print('N')