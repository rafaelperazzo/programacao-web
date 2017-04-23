# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

L=int(input('Digite o valor de L:'))
R=int(input('Digite o valor de R:'))
D=int(input('Digite o valor de D:'))
    
if R<50 or R==50:
    print('N')
    
elif L<R or L>R or L==R:
    print('N')

elif D==L or D==R:
    print('N')
    
elif D>=R and D<L:
    print('N')