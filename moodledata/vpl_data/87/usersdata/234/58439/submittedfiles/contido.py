# -*- coding: utf-8 -*-


def contador(c,d):
    cont=0
    for i in range(0,len(c),1):
        for g in range(0,len(d),1):
            if (c[i])==(d[g]):
                cont=cont+1
    return(cont)
    
c=[]
d=[]
m=int(input('Digite a quantidade de c:'))
l=int(input('Digite a quantidade de d:'))

for i in range(0,m,1):
    n=int(input('Digite o valor:'))
    c.append(n)
    
for i in range(0,l,1):
    j=int(input('Digite o valor:'))
    d,append(j)
    
print(contador(c,d))
    