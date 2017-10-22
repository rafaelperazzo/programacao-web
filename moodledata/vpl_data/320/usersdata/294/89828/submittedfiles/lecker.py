# -*- coding: utf-8 -*-
import math
n1= int(input('Insira o primeiro número: '))
n2= int(input('Insira o segundo número: '))
n3= int(input('Insira o terceiro número: '))
n4= int(input('Insira o quarto número: '))
c=0
i=1
for i in range(1,5,1):
    while 'n'+(i-1)<'n'+i<'n'+(i+1) or 'n'+i<'n'+(i+1) or 'n'+(i-1)<'n'+i:
        c=c+1
if c==1:
    print('S')
else:
    print('N')