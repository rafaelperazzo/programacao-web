# -*- coding: utf-8 -*-
import math
variavel1=int(input('digite a viariável 1:'))
variavel2=int(input('digite a viariável 2:'))
variavel3=int(input('digite a viariável 3:'))
variavel4=int(input('digite a viariável 4:'))
if variavel1>variavel2 and variavel4<=variavel3:
    print('s')
elif variavel1<variavel2 and variavel2>variavel3 and variavel4<=variavel3:
    print('s')
elif variavel1<=variavel2 and variavel2<variavel3 and variavel4<variavel3:
    print('s')
elif variavel1<=variavel2 and variavel2<=variavel3 and variavel4>variavel3:
    print('s')
else:
    print('n')
    