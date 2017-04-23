# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

L=int(input('Digite o valor de L:'))
R=int(input('Digite o valor de R:'))
D=int(input('Digite o valor de D:'))
    
if (R>50<100) and D<R:
    print('N')
    
elif R<50 or R>100:
    print('N')
    
elif D>R and D>L and L>R:
    print('N')
    
elif  D>R and D<L and L>R:
    print('N')
    
elif  D<R and R>L:
    print('N')
    
elif  R>L and D<L and D<R:
    print('N')
    
elif R<L and D>L and D<R:
    print ('N')
    
elif L<D>R:
    print('S')
    
else:
    print('N')
    
    
    

    

    