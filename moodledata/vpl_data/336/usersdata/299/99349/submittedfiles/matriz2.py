# -*- coding: utf-8 -*-
x=0
def analisemagica(x):
    c=0
    #analise de linhas
    for i in range(1,len(x)-1,1):
        if sum(x[i-1])==sum(x[i]):
            c=True
        else:
            c=False
            break
    #analise de colunas
    cont=[]
    for j in range(0,len(x)-1,1):
        for i  in range(1,len(x)-1,1):
            cont.append(x[i-1][j])
            
    for i in range(1,len(cont)-1,1):
        if sum(cont[i-1])==sum(cont[i]):
            c=True
        else:
            c=False
            break
    if c==True:
        return 'S'
    else:
        return 'N'
main=[]
linha=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        main.append(int(input(''))

if analisemagica(main)=='S':
    print('S')
else:
    print('N')



















