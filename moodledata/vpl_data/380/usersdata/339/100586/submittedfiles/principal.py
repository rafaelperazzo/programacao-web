# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
#from minha_bib import *
'''
tab=tabuleiro()
vencedor(tab)
'''
tab=[[],[],[]]
for i in range(0,3,1):
    for j in range(0,3,1):
        tab.append(tab[input(i)][input(j)])
        
print(tab)
