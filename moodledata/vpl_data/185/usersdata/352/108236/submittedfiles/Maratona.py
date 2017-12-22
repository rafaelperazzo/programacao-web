# -*- coding: utf-8 -*-

def maratona(a,dist):
    for i in range(0,len(a)-1,1):
        if (a[i+1]-a[i])>dist:
            return('N')
    return('S')
n=int(input('Quantidade de postos: '))