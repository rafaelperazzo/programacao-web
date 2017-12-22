# -*- coding: utf-8 -*-
import numpy as np

n = int(input('Digite a dimensão n da matriz nxn: '))
matriz = np.empty([n,n])

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz = float(input('Digite o termo[%d][%d] da matriz: ' %((j+1),(i+1))))
    
