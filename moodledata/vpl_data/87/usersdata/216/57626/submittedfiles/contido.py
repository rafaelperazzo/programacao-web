# -*- coding: utf-8 -*-


def contador(a,b):
    cont=0
    for i in range(0,len(a),1):
        for g in range(0,len(b),1):
            if (a[i])==(b[g]):
                cont=cont+1
    return(cont)
    
a=[]
b=[]

for i in range(0,m,1):
    n=int(input('Digite o valor:'))
    a.append(n)
    
for g in range(0,l,1):
    j=int(input('Digite o valor:'))
    b.append(j)
    

m=int(input('Digite a quantidade de a:'))
l=int(input('Digite a quantidade de b:'))
print(contador(m,l))

