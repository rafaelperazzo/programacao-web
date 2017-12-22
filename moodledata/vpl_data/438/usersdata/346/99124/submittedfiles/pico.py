# -*- coding: utf-8 -*-
def decrescente(n):
    cont=0
    for i in range(0,len(n)-1,1):
        if n[i] > n[i+1]:
            cont +=1
    if cont==len(n)-1:
        return True
    else:
        return False

n = int(input('Digite a quantidade de elementos da lista: '))
l= []
posicao= 0

for i in range(0,n,1):
    l.append(int(input('Digite um valor: ')))

for i in range(0, len(l)-1,1):
    if (l[i] > l[i+1]):
        posicao = l
        break

if decrescente(l[posicao:len(l)]):
    print ('S')
else:
    print('N')
        





