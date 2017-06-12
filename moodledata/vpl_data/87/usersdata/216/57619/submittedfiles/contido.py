# -*- coding: utf-8 -*-


m=int(input('Digite a quantidade de a:'))
l=int(input('Digite a quantidade de b:'))
a=[]
b=[]

for i in range(0,m,1):
    n=int(input('Digite o valor:'))
    a.append(n)
    
for g in range(0,l,1):
    j=int(input('Digite o valor:'))
    b.append(j)
def contador(a,b):
    for i in range(0,len(a),1):
        for g in range(0,len(b),1):
            cont=0
            if (a[i])==(b[g]):
                cont=cont+1
    return(cont)
    
m=int(input('Digite a quantidade de a:'))
l=int(input('Digite a quantidade de b:'))
print(contador(m,l))

