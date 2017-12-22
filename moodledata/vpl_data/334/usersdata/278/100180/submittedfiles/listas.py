# -*- coding: utf-8 -*-
n = int(input("Digite a quantidade de termos da lista x: "))
x = []
y = []
for i in range (0,n,1):
    x.append(int(input("Digite o elemento%.d da lista x: " %(i+1))))
for i in range (0,n,1):
    if i<(n-1):
        altura = x[i]-x[i+1]
        if altura<0:
            altura*=-1
        y.append(altura)
c=0
for i in range (0,n-1,1):
    for j in range (0,n-1,1):
        if y[i]>y[j]:
            z=i
        continue
        else:
            c+=1
            break
if c==0:
    print(z)
            
        

