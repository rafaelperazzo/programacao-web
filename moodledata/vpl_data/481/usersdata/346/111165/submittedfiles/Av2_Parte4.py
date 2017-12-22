# -*- coding: utf-8 -*-
n= int(input('Digite valor de n: '))

a=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(input('Valores da matriz: '))
    a.append(linha)

cont=0
for i in range(0,n,1):
    t=0
    cont=0
    for j in range(0,n,1):
        t= t + int(a[i][j])
        cont+=1
    d= t-int(a[i][i])
    cont +=1

maior=0
while int(a[i][i])>maior:
    maior= int(a[i][i])
    
if maior>d:
    print('SIM')
else:
    print('NAO')
    


 