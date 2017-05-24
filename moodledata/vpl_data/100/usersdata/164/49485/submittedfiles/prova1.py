# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
c1=int(input('Digite a primeira carta: '))
while (c1<1) or (c1>13):
    c1=int(input('Digite a primeira carta: '))
c2=int(input('Digite a segunda carta: '))
while (c2<1) or (c2>13):
    c2=int(input('Digite a segunda carta: '))
c3=int(input('Digite a terceira carta: '))
while (c3<1) or (c3>13):
    c3=int(input('Digite a terceira carta: '))
c4=int(input('Digite a quarta carta: '))
while (c4<1) or (c4>13):
    c4=int(input('Digite a quarta carta: '))
c5=int(input('Digite a quinta carta: '))
while (c5<1) or (c5>13):
    c5=int(input('Digite a quinta carta: '))
if (c1>c2>c3>c4>c5):
    print('D')
elif (c1<c2<c3<c4<c5):
    print('C')
else:
    print('N')
