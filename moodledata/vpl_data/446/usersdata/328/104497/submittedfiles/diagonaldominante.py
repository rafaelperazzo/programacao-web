# -*- coding: utf-8 -*-
d=int(input ('Digite a ordem da matriz:'))
m=[]
for i in range(d):
    l=[]
    for j in range(d):
        l.append(float(input('Dê valores a matriz:')))
    m.append(l)

s = 0
for i in range (d):
    s = s + m[i][i]

for i in range (d):
    n =0
    for j in range (d):
        n = n + m[i][j]
        if s < n:
            print('NAO')
            exit()
print('SIM')

    

