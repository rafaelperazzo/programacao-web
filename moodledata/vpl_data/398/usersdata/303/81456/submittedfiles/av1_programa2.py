# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
c1=int(input('VALOR DA PRIMEIRA CARTA:'))
c2=int(input('VALOR DA SEGUNDA CARTA:'))
c3=int(input('VALOR DA TERCEIRA CARTA:'))
c4=int(input('VALOR DA QUARTA CARTA:'))
c5=int(input('VALOR DA QUINTA CARTA:'))
c6=int(input('VALOR DA SEXTA CARTA:'))
if c1<c2 and c2<c3 and c3<c4 and c4<c5 and c5<c6:
    print('C')
if c1>c2 and c2>c3 and c3>c4 and c4>c5 and c5>c6:
    print('D')
