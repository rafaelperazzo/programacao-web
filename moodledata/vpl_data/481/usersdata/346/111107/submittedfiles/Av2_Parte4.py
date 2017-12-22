# -*- coding: utf-8 -*-
n= int(input('Digite valor de n: '))

a=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(input('Valores da matriz: '))
    a.append(linha)

cont=0
t=0    
for i in range(0,n,1):
    for j in range(0,n,1):
        t= t + int(a[i][j])-int(a[i][i])
        cont +=1

if int(a[i][j])>t:
    print('SIM')
else:
    print('NAO')
    
'''cont=0
som=0
for i in range(0,n,1):
    som= som + a[i][i]
    cont +=1
    
cont=0
l=0    
for i in range(0,n,1):
    l= l + a[i][j]
    cont +=1

if som>l:
    print('SIM')
else:
    print('NAO')
'''

 