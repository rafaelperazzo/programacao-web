# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
L= float(input('digite a posição do atacante que passa a bola:'))
R= float(input('digite a posição do atacante que recebe a bola:'))
D= float(input('digite a posição do último defensor advérsario:'))
 
if R>50 and L<R and R<D:
     print('S')
else:
     print('N')