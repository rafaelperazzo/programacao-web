# -*- coding: utf-8 -*-

def menos(a):
    menos=0
    l=[]
    for i in range(0,len(a)-1,1):
        menos=menos+(a[i]-a[i+1])
        if menos<0:
            menos=menos*(-1)
            l.append(menos)
        else:
            l.append(menos)
    return(l)
            

def maior(l):
    c=0
    for i in range(0,len(l)-1,1):
        if c>l[i]:
            c=l[i]
        else:
            c=l[i]
    return(c)
a=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(0,n,1):
    x=int(input('Digite o numero:'))
    a.append(x)
    
x=menos(a)
print (maior(x))
    
            
            
