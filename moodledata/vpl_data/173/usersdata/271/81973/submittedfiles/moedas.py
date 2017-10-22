# -*- coding: utf-8 -*-
#ENTRADA
moedasA = int(input('Digite o valor das moedas A : '))
moedasB = int(input('Digite o valor das moedas B : '))
cedulaC = int(input('Digite o valor da cedula c : '))

#PROCESSAMENTO
while (cedulaC>0) :
    qa = (cedulaC//moedasA)
    qb = (cedulaC%qa)//b
    cedulaC = cadulaC - (qa+qb)
    if (qa+qb) == cedulaC :
        print(qa)
        print(qb)
        print('S')
    else :
        print(qa)
        print(qb)
        print('N')
        

