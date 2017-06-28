# -*- coding: utf-8 -*-
def Degraus(a):
    b=[]
    for i in range(0,len(a)-1,1):
        diferença=abs(a[i]-a[i+1])
        b.append(diferença)
    return(b)
def Maior(a):
    Maior=a[0]
    for i in range(0,len(a),1):
        if a[i]>Maior:
            Maior=a[i]
        return Maior
def maiorDegrau(a):
    b=Degraus(a)
    m=Maior(b)
    return(m)
n=int(input('Tamanho dalista:'))
a=[]
for i in range(1,n+1,1):
    l=int('Digite o número:'))
    a.append(l)
print(Degraus(a))
print(maiorDegrau(a))
