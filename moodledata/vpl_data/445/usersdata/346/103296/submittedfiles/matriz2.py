# -*- coding: utf-8 -*-

n= int(input("Digite um valor: "))
m= []

for i in range(0,n,1):
    l= []
    for j in range(0,n,1):
        l.append(int(input('Digite um valor para a matriz: ')))
    m.append(l)
    
def magica(m):
    x= []
    for i in range(len(m)):
        soma1=0
        soma2=0
        for j in range(len(m[i])):
            soma1= soma1 + m[i][j]
            soma2= soma2 + m[j][i]
    soma1=o
    soma2=o
    c=1
    for i in range(len(m)):
        soma1= soma1 + m[i][i]
        soma2= soma2 + m[i][len(m)-c]
        c += 1
    x.append(soma1)
    x.append(soma2)
    
    for i in range(len(m)):
        if x[i] != x[1]:
            return False
    return True

if magica(m):
    print('S')
else:
    print('N')

