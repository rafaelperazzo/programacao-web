# -*- coding: utf-8 -*-
def degraus(a):
    b=[]
    for i in range(0,len(a)-1,1):
        diferenca=(a[i]-a[i+1])
        b.append(diferenca)
    return(b)
def maior(a):
    maior=a[0]
    for i in range(0,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return(maior)
n=int(input('digite n:'))
a=[]
for i in range(0,len(a),1):
    valor=int(input('digite o valor:'))
    a.append(valor)
print(maior(degraus(a)))

