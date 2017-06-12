# -*- coding: utf-8 -*-
def interseção (a,b):
    cont=0
    indice=0
    if len(a)<len(b):
        while indice<len(a):
            for j in range(0,len(b),1):
                if lista[indice]==b[j]:
                    cont=cont+1
            indice=indice+1
    else:
        while indice<len(b):
            for j in range(0,len(a),1):
                if b[indice]==a[j]:
                    cont=cont+1
            indice=indice+1
    return(cont)
n=int(input('digite n:'))
m=int(input('digite m:'))
listaa=[]
listab=[]
for i in range(n):
    a=float(input('digite a :'))
    listaa=listaa+[a]
for i in range(m):
    b=float(input('digite b:'))
    listab=listab+[b]
c=interseção(listaa,listab)
print(c)
    

            
