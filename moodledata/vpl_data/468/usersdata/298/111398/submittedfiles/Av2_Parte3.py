# -*- coding: utf-8 -*-
def media(lista):
    h=len(lista)
    soma=float(sum(lista))
    med=soma/h
    return med

def desv(lista):
    h=len(lista)
    soma=float(sum(lista))
    med=soma/h
    var=0
    for i in range (0, h, 1):
        var+=(lista[i]-med)**(2.0)
    s=((1.0/(h-1))*var)**(0.5)
    return s

m=int(input('Digite a quantidade de listas: '))
n=int(input('Digite a quantidade de elementos das listas: '))

mat=[]
for i in range (0, m, 1):
    mat.append([])

for i in range (0, m, 1):
    for j in range (0, n, 1):
    mat[i].append(float(input('Digite um elemento para a lista %d: ' % ((i+1)))))

for i in range (0, m, 1):
    med=media(mat[i])
    pad=desv(mat[i])
    print('%.2f' % med)
    print('%.2f' % pad)
    
