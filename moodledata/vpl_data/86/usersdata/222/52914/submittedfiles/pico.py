# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    


n = input('Digite a quantidade de elementos da lista: ')
subiu=False
desceu=False
subiu_novamente= False
anterior=int(input('anterior:'))
atual=int(input('atual:'))
i=2
if anterior<atual:
    subiu=True
while i<n and anterior<atual:
    anterior=atual
    atual=int(input('atual:')
    i+=1
if anterior>atual:
    desceu=True
while i<n and anterior>atual:
    anterior=atual
    atual=int(input('atual:')
    anterior=atual
    
