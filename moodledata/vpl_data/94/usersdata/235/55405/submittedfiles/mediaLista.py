# -*- coding: utf-8 -*-
def lista(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+lista[i]
    media=soma/len(a)
    return(media)
n=int(input('digite o numero de elemetos da lista:'))
x=[]
for i in range(1,n+1,1):
    y=float(input('digite um elemento:'))
    x.append(y)
print('%.2f'%lista[0])
print('%.2f'%lista[len(a)-1])
print('%.2f'%media)
print(x)