# -*- coding: utf-8 -*-
import math

#ENTRADA
valor=int(input('Digite o valor: '))
#PROCESSAMENTO/SAIDA
cedulas=0
valorcedulaatual=20
valorcedulaaserentregue=valor
while True:
    if valorcedulaatual <=valoraserentregue:
        cedulas +=1
        valoraserentregue -= valorcedulaatual
    else:
        if cedulas > 0:
            print('%d cedula (s) de R$: %5.2f' % (cedulas, valorcedulaatual))
        if valoraserentregue == 0:
            break
        if valorcedulaatual == 20:
            valorcedulaatual = 10
        elif valorcedulaatual == 10:
            valorcedulaatual = 5
        elif valorcedulaatual == 5:
            valorcedulaatual = 2
        elif valorcedulaatual == 2:
            valorcedulaatual = 1
        cedulas=0

