# -*- coding: utf-8 -*-

def degraus(a):
    b=[]
    for i in range(0,len(a)-1,1):
        diferença=abs(a[i]-a[i+1])
        b.append(diferença)
    return(b)
def maior(a):
    maior=a[0]
    for i in range(0,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return maior
def maiordegrau(a):
    b=degraus(a)
    m=maior(b)
    return(m)
     lista=[]
n=int(input('tamanho da lista:'))
lista=[]
for i in range(1,n+1,1):
    valor=float(input('valor:'))
    lista.append(valor)
print(maiordegrau(lista))

