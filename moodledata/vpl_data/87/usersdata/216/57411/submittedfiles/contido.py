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
    1234 456
for i in range(0,len(a),1):
    cont=0
    if (i==0):
        if (a[i])==(b[g]):
            cont=cont+1 
            g=g+1
    elif (i==len(a)):
        if (a[i])==(b[g]):
            cont=cont+1 
            g=g+1
    else:
        if (a[i])==(b[g]):
            cont=cont+1
            g=g+1
    
        
print(cont)
print(a)
print(b)
