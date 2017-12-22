# -*- coding: utf-8 -*-
import numpy as np

n = int(input('Digite a dimensão n da matriz nxn: ')
matriz=[]

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i][j].append(input('Digite o termo[%d] da matriz: ' %((j+1),(i+1))))
    
