# -*- coding: utf-8 -*-

def diferenca(a):
    l=[]
    for i in range(0,len(a)-1,1):
        menos=(a[i]-a[i+1])
        if menos<0:
            menos=menos*(-1)
            l.append(menos)
        else:
            l.append(menos)
    return(l)
            

def maior(l):
    c=0
    for i in range(0,len(l),1):
        if (l[i])>(l[i+1]):
            c=l[i]
    return(c)

a=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(0,n,1):
    x=int(input('Digite o numero:'))
    a.append(x)
    
j=diferenca(a)

print(maior(j))
    
            
            
