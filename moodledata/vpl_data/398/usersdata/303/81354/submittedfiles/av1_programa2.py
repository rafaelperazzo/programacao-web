# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
carta1=int(input('VALOR DA PRIMEIRA CARTA:'))
carta2=int(input('VALOR DA SEGUNDA CARTA:'))
carta3=int(input('VALOR DA TERCEIRA CARTA:'))
carta4=int(input('VALOR DA QUARTA CARTA:'))
carta5=int(input('VALOR DA QUINTA CARTA:'))
carta6=int(input('VALOR DA SEXTA CARTA:'))
if carta1<carta2 and carta2<carta3 and carta3<carta4 and carta4<carta5 and carta5<carta6:
    print('C')
if carta1>carta2 and carta2>carta3 and carta3>carta4 and carta4>carta5 and carta5>carta6:
    print('D')
if carta1>carta2 and carta2>carta3 and carta3>carta4 and carta4>carta5 and carta5<carta6:
    print('N')
if carta1>carta2 and carta2>carta3 and carta3>carta4 and carta4<carta5 and carta5<carta6:
    print('N')
if carta1>carta2 and carta2>carta3 and carta3<carta4 and carta4<carta5 and carta5<carta6:
    print('N')
if carta1>carta2 and carta2<carta3 and carta3<carta4 and carta4<carta5 and carta5<carta6:
