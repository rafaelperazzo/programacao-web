# -*- coding: utf-8 -*-
def Degraus(a):
    b=[]
    for i in range(0,len(a)-1,1):
        diferença=abs(a[i]-a[i+1])
        b.append(diferença)
    return(b)  
def Maior(b):
    Maior=b[0]
    for i in range(0,len(b),1):
        if a[i]>Maior:
            Maior=a[i]
    return Maior        
n=int(input('Tamanho da lista: '))
a=[]
for i in range(1,n+1,1):
    l=int(input(' Digite o número: '))
    a.append(l)
print(a)
print(Maior(b))