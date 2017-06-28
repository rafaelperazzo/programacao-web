# -*- coding: utf-8 -*-
def maior(a):
    maior=a[0]
    for i in range(0,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return(maior)
def degraus(a):
    b=[]
    for i in range(0,len(a)-1,1):
        dife=abs(a[i]-a[i+1])
        b.append(dife)
    return(b)
def maiordegrau(a):
    b=degraus(a)
    m=maior(b)
    return(m)
lista=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(1,n+1,1):
    v=float(input('Digite o valor:'))
    lista.append(v)
print(maiordegrau(lista))

