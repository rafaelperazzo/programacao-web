# -*- coding: utf-8 -*-
def degraus(a):
    b=[]
    for i in range (0,len(a)-1,1):
        diferenca=abs(a[i]-a[i+1])
        b.append(diferenca)
    return(b)
def maior(a):
    maior=a[0]
    for i in range (1,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return(maior)
def maiordegrau(a):
    b=degraus(a)
    m=maior(b)
    return(m)
n=int(input('digite n:'))
a=[]
for i in range (0,n,1):
    valor=int(input('digite o valor:'))
    a.append(valor)
print(maiordegrau(a))    
