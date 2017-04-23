# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

L=int(input('Digite o valor de L:'))
R=int(input('Digite o valor de R:'))
D=int(input('Digite o valor de D:'))

if R>50:
    print('S')
    
elif R<50:
    print('N')
    
elif L<R:
    print('N')

elif R==50:
    print('N')
    
elif D>=R and D>=L:
    print('N')
    
elif D>R:
    print('N') 
    