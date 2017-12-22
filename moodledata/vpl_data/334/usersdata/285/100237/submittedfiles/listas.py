# -*- coding: utf-8 -*-
def modulo_diferença(x,y):
    dif=x-y
    if dif<0:
        dif=fid*(-1)
        return(dif)
    else:
        return(dif)
lista=[]
degrau=0
n=int(input("Digite o número de elementos da lista: "))
while(True):
    if n<2:
        n=int(input("Digite o número de elementos da lista: "))
        else:
            break
for i in range(0,n,1):