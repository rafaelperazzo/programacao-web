# -*- coding: utf-8 -*-
n=int(input('digite a dimensao da matriz: '))
m=[]
for i in range(0,n,1):
    colunas=[]
    for j in range(0,n,1):
        colunas.append(float(input('digite um termo da matriz: ')))
    m.append(colunas)
i=0
j=0
if m[i][j]>m[i][j+1] and m[i][j]>m[i][j+2]:
        if m[i+1][j+1]>m[i][j] and m[i+1][j+1]>m[i+2][j+2]:
            if m[i+2][j+2]>m[i][j] and m[i+2][j+2]>m[i+1][j+1]:
                print('sSIM')
            else:
                print('NAO')
        else:
                print('NAO')
else:
                print('NAO')
    
