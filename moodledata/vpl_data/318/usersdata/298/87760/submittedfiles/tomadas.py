# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
t1 = int(input('Digite o número de tomadas da régua 1: '))
t2 = int(input('Digite o número de tomadas da régua 2: '))
t3 = int(input('Digite o número de tomadas da régua 3: '))
t4 = int(input('Digite o número de tomadas da régua 4: '))

while t1<=1:
    t1=int(input('Entrada inválida. Digite o número de tomadas da régua 1: '))
if t1>1:
    while t2<=1:
        t2=int(input('Entrada inválida. Digite o número de tomadas da régua 2: '))
    if t2>1:
        while t3<=1:
            t3=int(input('Entrada inválida. Digite o número de tomadas da régua 3: '))
        if t3>1:
            while t4<=1:
                t4=int(input('Entrada inválida. Digite o número de tomadas da régua 4: '))
            if t4>1:
                k=(t1+t2+t3+t4)-3
                print(k)