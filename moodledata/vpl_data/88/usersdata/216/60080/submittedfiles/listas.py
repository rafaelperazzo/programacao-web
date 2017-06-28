# -*- coding: utf-8 -*-

def :
    l=[]
    for i in range(0,len(a)-1,1):
        menos=a[i]-a[i+1]
        if menos<0:
            menos=menos*(-1)
            l.append(menos)
        else:
            l.append(menos)
    return(l)

def maior(a):
    for i in range(0,len(a),1):
        if a[i]<a[i+1]:
            i=i+1
        else:
            cont=a[i]
    return(cont)

a=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(0,n,1):
    x=int(input('Digite o numero:'))
    a.append(x)
    
m=diferenca(a)
print(maior(diferenca(m)))