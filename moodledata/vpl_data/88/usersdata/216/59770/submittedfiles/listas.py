# -*- coding: utf-8 -*-

def soma(a):
    for i in range(0,len(a)-1,1):
        menos=0
        l=[]
        menos=menos+(a[i]-a[i+1])
        if menos<0:
            menos=menos*(-1)
            l.append(menos)
        else:
            l.append(menos)
            
l=degrau(a)
def maior(l):
    for i in range(0,len(l)-1,1):
        maior=0
        if l[i]>l[i+1]:
            maior=a[i]
        return(a[i])
a=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(0,n,1):
    x=int(input('Digite o numero:'))
    a.append(x)
    

print (maior(a))
    
            
            
