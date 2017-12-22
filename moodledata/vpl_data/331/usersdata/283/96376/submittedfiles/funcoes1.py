# -*- coding: utf-8 -*-
a=[]
b=[]
c=[]
d=0
n=int(input('Digite o número de elementos: '))
for i in range (0,n,1):
    a.append(input('a[%d]: '%(i+1)))
for i in range (0,n,1):
    b.append(input('b[%d]: '%(i+1)))
for i in range (0,n,1):
    c.append(input('c[%d]: '%(i+1)))
    #escreva o código da função crescente aqui
def crescente(a):
    for i in range (0,n,1):
        if a[i]<a[i+1]:
            d+=1
            if (i+1)>n:
                break
                return d
            
            
    

#escreva as demais funções





#escreva o programa principal

if d==(n-1):
    print(crescente(a))
