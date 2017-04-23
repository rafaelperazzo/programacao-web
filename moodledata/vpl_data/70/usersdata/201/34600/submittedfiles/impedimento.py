# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L=int(input('Digite um valor:'))
R=int(input('Digite um valor:'))
D=int(input('Digite um valor:'))
L>=0 and L<=100
R>=0 and R<=100
D>=0 and D<=100
if R>50 and L<R and R>D:
    print('S')
else:
    print('N')