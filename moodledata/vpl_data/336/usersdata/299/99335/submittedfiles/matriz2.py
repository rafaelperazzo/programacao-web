# -*- coding: utf-8 -*-
main=[]
linha=[]
n=int(input(''))
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        main.append(int(input(''))
def analisemagica(x):
    c=0
    #analise de linhas
    for i in range(1,len(x)-1,1):
        if sum(x[i-1])==sum(x[i]):
            c=True
        else:
            c=False
            break
            
