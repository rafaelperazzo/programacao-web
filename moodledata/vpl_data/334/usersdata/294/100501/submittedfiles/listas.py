# -*- coding: utf-8 -*-
def modulo_diferenca(x,y)
    dif=x-y
    if dif<0:
        dif*=(-1)
        return(dif)
    else:
        return(dif)

n= int(input('Digite o número de elementos: '))
while n<2:
    n= int(input('Digite o número de elementos: '))
    
a=[]
degrau=0

for i in range (0,n,1):
    a.append(int(input('Digite o elemento%d: ' %(i+1))))
for i in range (0,n-1,1):
    if modulo_diferenca(a[i],a[i+1])>degrau:
        degrau=modulo_diferenca(a[i],a[i+1])

print(degrau)
