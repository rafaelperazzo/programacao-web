# -*- coding: utf-8 -*-
def maiorAltura(a):
    resultado=abs(a[0]-a[1])
    for i in range(0,len(a)-1,1):
        if abs(a[1]-a[i+1])>resultado:
            resultado=abs(a[i]-a[i+1])
    return (resultado)
    
n=int(input('digite n:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite o valor:'))
    a.append(valor)
maiorDegrau=maiorAltura(a)
print(maiorDegrau)
