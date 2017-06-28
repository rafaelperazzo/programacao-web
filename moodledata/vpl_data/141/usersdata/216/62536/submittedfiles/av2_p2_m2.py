# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de salas:'))
a=[]
for i in range(0,n,1):
    x=int(input('Digite a quantidade de vidas:'))
    a.append(x)

def somatorio(a,x,y):
    for i in range(x,y+1,1):
        soma=0
        soma=soma+a[i]
    return(soma)
    
print(a)
x=int(input('Digite a entrada:'))
y=int(input('Digite a saida:'))   

