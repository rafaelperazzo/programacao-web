# -*- coding: utf-8 -*-
n= int(input("digite a ordem do tabuleiro: "))
tabuleiro=[]
for i in range(0,n,1):
    tabuleiro_linha=[]
    for j in range(0,n,1):
        tabuleiro_linha.append(int(input("digite o valor (%d,%d): " %(i+1,i+1))))
        

