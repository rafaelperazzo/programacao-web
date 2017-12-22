# -*- coding: utf-8 -*-
import numpy as np
m = int(input('Digite o valor de m: '))
n = int(input('Digite o valor de n: '))
a = np.empty
for i in range(0,m,1):
    for j in range(0,n,1):
        a[i][j] = float(input(Digite %d e %d: ' % ((j+1),(i+1))))
print(a)        




