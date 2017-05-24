# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
carta1=int(input('digite o valor da carta1:'))
carta2=int(input('digite o valor da carta2:'))
carta3=int(input('digite o valor da carta3:'))
carta4=int(input('digite o valor da carta4:'))
carta5=int(input('digite o valor da carta5:'))

if (carta1>carta2>carta3>carta4>carta5):
    print ('c')
elif (carta1<carta2<carta3<carta4<carta5):
    print ('d')
else:
    print ('n')
