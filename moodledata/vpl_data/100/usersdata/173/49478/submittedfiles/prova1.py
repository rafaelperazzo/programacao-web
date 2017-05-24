# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA
n1=int(input('Digite o valor da primeira carta: '))
n2=int(input('Digite o valor da segunda carta: '))
n3=int(input('Digite o valor da terceira carta: '))
n4=int(input('Digite o valor da quarta carta: '))
n5=int(input('Digite o valor da quinta carta:' ))
if(n1<n2)and(n2<n3)and(n3<n4)and(n4<n5):
    print('C')
elif(n1>n2)and(n2>n3)and(n3>n4)and(n4>n5):
    print('D')
else:
    print('N')