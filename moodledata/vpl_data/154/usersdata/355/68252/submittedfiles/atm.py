# -*- coding: utf-8 -*-
import math

#ENTRADA
valor=int(input('Digite o valor: '))
#PROCESSAMENTO/SAIDA
cedulas=0
valorcedulaatual=20
valoraserentregue=valor
while True:
    if valorcedulaatual <=valoraserentregue:
        cedulas +=1
        valoraserentregue -= valorcedulaatual
    else:
        if cedulas > 0:
            print(cedulas)
        if valoraserentregue == 0:
            break
        if valorcedulaatual == 20:
            valorcedulaatual = 10
        elif valorcedulaatual == 10:
            valorcedulaatual = 5
            print(cedulas)
        elif valorcedulaatual == 5:
            valorcedulaatual = 2
            print(cedulas)
        elif valorcedulaatual == 2:
            valorcedulaatual = 1
        cedulas=0

