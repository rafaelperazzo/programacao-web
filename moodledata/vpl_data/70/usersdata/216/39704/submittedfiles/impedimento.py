# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Digite a posição:'))
R=int(input('Digite a posição:'))
D=int(input('Digite a posição:'))

if R>50:
    print('S')
elif L<R:
    print('S')
elif R>D:
    print('S')
else:
    print('N')
