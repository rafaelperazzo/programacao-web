# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
l=int(input('Digite a posição do lançador: '))
r=int(input('Digite a posição do recebedor: '))
d=int(input('Digite a posição do defensor: '))
if(r<=50):
    print('N')
elif(r>50)and(l>r):
    print('N')
elif(r>50)and(r<d):
    print('N')
else:
    print('S')