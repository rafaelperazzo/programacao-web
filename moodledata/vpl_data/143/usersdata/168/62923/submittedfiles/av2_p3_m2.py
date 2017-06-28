# -*- coding: utf-8 -*-
def degrau(p,q):
    for i in range (0,n-1,1):
        q.append(a[i]-a[i+1])
    for i in range (0, len(b),1):
        if (b[i]<0):
            b[i]=b[i]*(-1)
        return (b)

n=int(input('Digite a quantidade de termos: '))
p=[]
q=[]
for i  in range (0,n,1):
    valor=int(input('Digite o valor da lista: '))
    p.append(valor)
print(degrau(p,q))    



