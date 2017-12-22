# -*- coding: utf-8 -*-

n=int(input('Digite a quantidade de números: '))
a=[]
somapar=0
somaimpar=0
p=0
y=0
for i in range(0,n,1):
    a.append(int(input('Digite um valor: ')))
    if(a[i]%2==0):
        somapar += a[i]
    if(a[i]%2==1):
        somaimpar += a[i]
print('soma dos ímpares: %d' %somaimpar)        
print('soma dos pares: %d' %somapar)

for i in range(0,n,1):
    if(a[i]%2==1):
        y += a[i]/a[i]
print('quantidade ímpares: %d' %y)
for i in range(0,n,1):
    if(a[i]%2==0):
        p += a[i]/a[i]
print('quantidade de pares: %d' %p)

        
    

        
