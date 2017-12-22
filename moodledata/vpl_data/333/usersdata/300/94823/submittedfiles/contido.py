# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de elementos de a: '))
m = int(input('Digite a quantidade de elementos de b: '))
a = []
b = []
def contagem(n,x,y):
    cont = 0
    for i in range (0,n,1):
        if x[i] in y:
            cont = cont + 1
    return cont        
for i in range (0,n,1):
    a.append(int(input('Digite os elementos de a: ')))
for i in range (0,m,1):
    b.append(int(input('Digite os elementos de b: ')))    
    
print(contagem(n,a,b))        
