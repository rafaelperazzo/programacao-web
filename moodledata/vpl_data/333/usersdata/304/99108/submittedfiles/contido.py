# -*- coding: utf-8 -*-
'''
def contido(lista1,lista2):
    cont_contido = 0
    
    for i in range(0,len(lista2),1):
        if lista2[i] in lista1:
            cont_contido = cont_contido+1
    return(cont_contido)
listaa=[]
listab=[]
n1=int(input('N: '))
n2=int(input('N: '))

for i in range(0,n1,1):
    listaa.append(int(input('N: '))
for i in range(0,n2,1):
    listab.append(int(input('N: '))

print(contido(listaa,listab))
'''
a = []
b = []
cont = 0
n_a = int(input('Na: '))
n_b = int(input('Nb: '))
for i in range (0,n_a,1):
    v_a = int(input('A: '))
    a.append(v_a)
for i in range (0,n_b,1):
    v_b = int(input('b: '))
    b.append(v_b)

for i in range(0,n_a,1):
    for j in range(0,n_b,1):
        if a[i] == b[j]:
            cont = cont+1
print(cont)
    
