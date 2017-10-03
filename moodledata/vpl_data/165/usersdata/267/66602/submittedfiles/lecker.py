# -*- coding: utf-8 -*-
import math
a = float(input('Digite o 1º número: '))
b = float(input('Digite o 2º número: '))
c = float(input('Digite o 3º número: '))
d = float(input('Digite o 4º número: '))
print()
print('Verificação de LECKER. S = Sim, N = Não: ')
if a>b:
    if b>=c>=d:
        print('S')
    else:
        if a<b>c:
            if c>=d:
                print('S')
            else:
                if b<c>d:
                    if a<=b:
                        print('S')
                    else:
                        if d>c:
                            if a<=b<=c:
                                print('S')
                            else:
                                print('N')


    