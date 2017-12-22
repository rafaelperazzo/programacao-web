# -*- coding: utf-8 -*-
import numpy as np
c1 = 0
c2 = 0
c3 = 0
n = int(input('Digite a dimensão da matriz: '))

while (n<2):
    n = int(input('Digite a dimensão da matriz: '))
m = np.empty([n,n])
mt = np.empty([n,n])
md = np.empty([2,n])
mp = np.empty([n,n])

for i in range(n):
    for j in range(n):
        m[i][j]=float(input('Digite o valor na linha %d e na coluna %d: ' %((i+1),(j+1))))
        
for i in range(n):
    for j in range(n):
        mt[i][j]=m[j][i]

for i in range(n):
    for j in range(n):
        mp[i][j] = m[i][n-1-j]

for i in range(n):
    md[0][i] = m[i][i]
for i in range(n):
    md[1][i] = mp[i][i]
    
for i in range(n-1):
    if sum(m[i]) == sum(m[i+1]):
        c1 = c1 + 1   
    
for i in range(n-1):
    if sum(mt[i]) == sum(mt[i+1]):
        c2 = c2 + 1
        
if sum(md[0]) == sum(md[1]):
    c3 = c3 + 1
    
if c1 == n-1 and c2 == n-1 and c3 == 1:
    print('S')
else:
    print('N')
