# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
#ENTRADA
l = float(input('Digite a posição do lançador: '))
r = float(input('Digite a posição do recebedor: '))
d = float(input('Digite a posição do defensor: '))
#PROCESSAMENTO
if r>50 and r>l and r>d :
    print('S')
else :
    print('N')
