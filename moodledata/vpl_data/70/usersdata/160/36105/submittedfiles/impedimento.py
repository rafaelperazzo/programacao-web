# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI

L=int(input('Digite o valor de L:'))
R=int(input('Digite o valor de R:'))
D=int(input('Digite o valor de D:'))
    
if L<R and R<D:
    print('S')
    
elif L<R and R>D>=L:
    print('N')
    
if L>R and L>D:
    print('N')
    
if L>R and L<D:
    print('N')
    
    
    
    
    

    

    