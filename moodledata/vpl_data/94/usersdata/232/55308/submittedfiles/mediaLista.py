# -*- coding: utf-8 -*-
def media (lista):
    soma=0
    for i in range (0,len(lista)-1,1):
        soma=soma+lista[i]
    return soma
    
n=int(input('Digite o número de elementos da lista: '))
a=[ ]
for i in range (1,n+1,1):
    h=float(input('Digite o elemento '+str(i)+' da lista: '))
    a.append(h)    

print('%.2f' %a[0])
print('%.2f' %a[len(a)-1])
print('%.2f' %media(a))
print(a)

