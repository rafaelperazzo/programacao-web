# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de numeros: '))
a=[]
impar=[]
par=[]  
for i in range(0,n,1):
    a.append(int(input('Digite o numero%d:' %(i+1))))
for i in range(0,n,1):
    if a[i]%2==0:
        par.append(a[i])
    else:
        impar.append(a[i])
print((sum(impar)))
print((sum(par)))
print((len(impar)))
print((len(par)))
print (a)
    

