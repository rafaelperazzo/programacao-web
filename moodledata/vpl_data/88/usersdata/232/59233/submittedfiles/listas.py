# -*- coding: utf-8 -*-
def Maior(a):
    maior=a[0]
    for i in range(1,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return (maior)
    
def degraus(a):
    b=[]
    for i in range(0,len(a)-1,1):
        diferença=abs(a[i]-a[i+1])
        b.append(diferença)
    return(b)
    
def MaiorDegrau(a):
    b=degraus(a)
    m=Maior(b)
    return(m)

n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(1,n+1,1):
    h=int(input('Digite o elemento '+str(i)+' da lista: '))
    a.append(h)
print(MaiorDegrau(a))
    

