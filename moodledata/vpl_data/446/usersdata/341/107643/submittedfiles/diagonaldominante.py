# -*- coding: utf-8 -*-

n = int(input('Digite a ordem da matriz: '))
m = []
for i in range(0, n, 1):
    l = []
    for j in range (0, n, 1):
        val = int(input('Digite os elementos: '))
        l.append(val)
    m.append(l)
if m[i][j] > (sum(m[i])-m[i][i]):
    print('SIM')
else:
    print('NAO')


