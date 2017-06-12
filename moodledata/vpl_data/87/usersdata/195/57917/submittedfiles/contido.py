# -*- coding: utf-8 -*-
def quantidade (a,b):
    cont=0
    for i in range (0,len(a),1):
        if a[i] in b:
            cont=cont+1
            a.appeend(a[i])
        return(cont)
n=int(input('digite o valor de n:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('digite o valor:'))
    a.append(valor)
m=int(input('digite o valor de m:'))
b=[]
for i in range(1,m+1,1):
    valor=float(input('digite o valor:'))
    b.append(valor)
print(quantidade (a,b))
            
