# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
carta1=int(input('digite o valor da carta1: '))
carta2=int(input('digite o valor da carta2: '))
carta3=int(input('digite o valor da carta3: '))
carta4=int(input('digite o valor da carta4: '))
carta5=int(input('digite o valor da carta5: '))
#PROCESSAMENTO

if carta1<carta2<carta3<carta4<carta5:
    print('C')

elif carta5>carta4>carta3>carta2>carta1:
    print('D')
else:
    print('N')



