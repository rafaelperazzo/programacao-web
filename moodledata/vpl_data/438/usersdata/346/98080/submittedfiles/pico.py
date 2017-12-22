# -*- coding: utf-8 -*-
lista= []
def pico(lista):
    #CONTINUE...
  


    n = int(input('Digite a quantidade de elementos da lista: '))
#CONTINUE...
    anterior= int(input('Digite um num: '))
    atual= int(input('Digite um num: '))
    
    no_picos= 0
    no_vales= 0
    
    i=2
    while i<n:
        prox= int(input('Digite um num: '))
        if anterior < atual > prox:
            no_picos +=1
        elif anterior > atual < prox:
            no_vales += 1
        
        anterior=atual
        atual=prox
        i += 1
    if no_picos == 1 and no_vales == 0:
        print('S')
    else:
        print('N')
