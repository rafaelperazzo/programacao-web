# -*- coding: utf-8 -*-
def interseção(a,b):
    cont=0
    indice=0
    if len(a)<len(b):
        while indice<len(a):
            for j in range(0,len(b),1):
                if listaindice==b[j]:
                    con=cont+1
            indice=indice+1
    else:
        while indice<len(b):
            for j in range(0,len(a),1):
                if listaindice==a[j]:
                    cont=cont+1
            indice=indice+1
    return(cont)
n=int(input('digite n:'))
m=int(input('digite m:'))
d=[]
f=[]
for i in range(n):
    d=int(input('digite d:'))
    d=d+[a]
for i in range(m):
    f=int(input('digite f:'))
    f=f+[a]
c=interseção(d,f)
print(c)
    
    
    