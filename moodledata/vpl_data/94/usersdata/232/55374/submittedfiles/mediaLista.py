# -*- coding: utf-8 -*-
def medialista (a):
    soma=0
    for i in range (0,len(a)-1,1):
        soma=soma+a[i]
    media=soma/(len(a)
    return media
    
n=int(input('Digite o número de elementos da lista: '))
a=[ ]
for i in range (1,n+1,1):
    h=float(input('Digite o elemento '+str(i)+' da lista: '))
    a.append(h)    

print('%.2f' %a[0])
print('%.2f' %a[len(a)-1])
print('%.2f' %media(a))
print(a)

