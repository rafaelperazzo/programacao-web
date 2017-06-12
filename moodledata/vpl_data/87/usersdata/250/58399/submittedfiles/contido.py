# -*- coding: utf-8 -*-
def interseccao(a,b):
    cont=0
    for i in range (0,len(a),1):
        if a[i] in b:
            cont=cont+1
    return (cont)
a=[]
b=[]
n=int(input('quantidade de elementos de a:'))
m=int(input('quantidade de elementos de b:'))
for i in range (0,n,1):
    a.append(int(input('elementos de a:')))
for i in range (0,m,1):
    b.append(int(input('elementos de b:')))
resultado=interseccao(a,b)
if resultado!=0:
    print('%d'%resultado)
else:
    print('nao existe numeros iguais!')
