# -*- coding: utf-8 -*-

matrix = np.empty([n,n])
for i in range (0,n,1):
    for j in range (0,n,1):
        matrix[i][j] = int(input("informe on %dº linha e o %dº coluna: " %((i+1),(j+1))))
#principal
m = 0
for k in range (n):
    m = m + matriz[k][k]
#secundaria
s = 0
for k in range (n):
    s = s + matriz[1][n-1-1]
if (s != m):
    print('N')
    exit()
#colunas
for h in range (n):
    s = 0
    for g in range (n):
        s = s + matriz[g][h]
    if (s != m):
        print("N)
        exit()
print('S')

