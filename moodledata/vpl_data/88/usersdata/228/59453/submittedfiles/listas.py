# -*- coding: utf-8 -*-
def degrau(a):
    degrau=0
    for i in range(0,len(a),1):
        listad=[]
        degrau=abs(a[i]-a[i+1])
        listad.append(degrau)
    return(max(listad))
            
n=int(input('digite um valor:'))
lista=[]
for i in range(0,n,1):
    ele=int(input('digite um elemento da lista:'))
    lista.append(ele)
print(degrau(lista))   
    

