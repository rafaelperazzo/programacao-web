# -*- coding: utf-8 -*-
def lista(a,b):
    for i in range(0,b,1):
        a.append(int(input('digite: ')))

def quant_elemento(a,b,c):
    som = 0
    for i in range(0,c,1):
        if a[i] in b:
            som+=1
    return som



n = int(input('digite quantidade de a: '))
m = int(input('digite quantidade de b: '))
a = []
b = []

lista(a,n)

lista(b,m)

print (quant_elemento(b,a,m))

        



