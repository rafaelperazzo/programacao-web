# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

L=int(input('Digite o valor de L:'))
R=int(input('Digite o valor de R:'))
D=int(input('Digite o valor de D:'))
    
if (R>50<L) or (R==50<=L) or (R<100):
    print('S')
    
elif R<50 or R>100:
    print('N')
    
elif D>R and D>L or D>R and D<L  or D<R and R>L or R>L and D<L and D<R:
    print('N')
    
elif L<D>R:
    print('N')
    
else:
    print('N')
    
    
    

    

    