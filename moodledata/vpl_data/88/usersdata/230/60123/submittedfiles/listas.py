# -*- coding: utf-8 -*-
def degrau(a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i-1]<a[i]:
            cont=cont+1
            return True
    
a=[]
n=int(input('Digite quantidade de números: '))
for i in range (0,n,1):
    valor=int(input('Digite valor: '))
    a.append(valor)

print(cont)
