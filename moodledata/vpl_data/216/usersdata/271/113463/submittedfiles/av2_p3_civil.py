# -*- coding: utf-8 -*-
import numpy as np
#ENTRADA
m = []
n = int(input('Digite a ordem da matriz : '))
while (n<3) :
    n = int(input('Digite a ordem da matriz : '))
for i in range (0,n,1) :
    linha = []
    for j in range (0,n,1) :
        ntrans[j][i] = m[i][j]
        
total = sum(m[0]) + sum(ntrans[0]) - 2*(m[0][0])
for i in range (0,n,1) :
    for j in range (0,n,1) :
        if total > sum(m[i]) + sum(ntrans[j]) - 2*(m[i][j]) : 
            total = total
        else :
            total = sum(m[i]) + sum(ntrans[j]) - 2*(m[i][j])
print(int(total))
    

