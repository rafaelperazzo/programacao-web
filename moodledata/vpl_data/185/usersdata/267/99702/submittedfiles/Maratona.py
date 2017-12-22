# -*- coding: utf-8 -*-

def maratona(x,dist):
    for i in range(0,len(x)-1,1):
        if (x[i+1]-x[i])>dist:
            return('N')
    return('S')

n=int(input('Número de postos: '))
m=int(input('Distância máxima para o atleta: '))
postos=[]
for i in range(0,n,1):
    postos.append(int(input('Digite a posição do posto: ')))
print(maratona(postos,m))