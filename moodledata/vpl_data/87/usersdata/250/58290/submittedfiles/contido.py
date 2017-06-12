# -*- coding: utf-8 -*-
def interseccao(a,b):
    cont=0
    for i in range (0,len(a),1):
        if a[i] in b:
            cont=cont+1
            
    return (cont)
a=[]
b=[]
n=int(input('valores da 1 lista:'))
for i in range (0,n,1):
    valores=int(input('valores:'))
    a.append(valor_a)
m=int(input('valores da 2 lista:'))
for i in range (0,m,1):
    valores=int(input('valores:'))
    b.append(valor_b)
resultado=interseccao(a,b)
if resultado!=0:
    print('%d'%resultado)
else:
    print('nao existe numeros iguais!')
