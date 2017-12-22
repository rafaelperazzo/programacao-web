# -*- coding: utf-8 -*-

def pico(lista):
    n = input('Digite a quantidade de elementos da lista: ')
    ant=int(input('digite um numero:'))
    atu=int(input('digite um numero:'))
    sp=0
    sv=0
    i=2
    while i<n:
        prox=int(input('digite um numero:'))
        if ant<atu>prox:
            sp+=1
        elif ant>atu<prox:
            sv+=1
        ant=atu
        atu=prox
        i+=1
    if sp==1 and sv==0:
        print('S')
    else:
        print('N')
        