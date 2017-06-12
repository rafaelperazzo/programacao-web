# -*- coding: utf-8 -*-
import math

#comece abaixo
def media (lista):
    m=0
    for i in range(0,len(lista),1):
        m=m+lista[i]
    o=m/len(lista)
    return o

def desvio (lista):
    p=0
    for i in range(0,len(lista),1):
        p=p+((lista[i]-media(lista))**2)
    k=((p/len(lista))**(1/2))
    return k
        
    

n=int(input("Digite o valor de n: "))
a=[]
for i in range(0,n,1):
    a.append(float(input("Digite o termo: ")))
print(a[0])
print(a[len(a)-1])
print(media(a))
print(desvio(a))
print(a)