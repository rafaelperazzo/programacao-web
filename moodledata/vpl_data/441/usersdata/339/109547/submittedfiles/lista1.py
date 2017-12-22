# -*- coding: utf-8 -*-

n=int(input('Quant. de elementos: '))
L=[]
p=0
i=0
qp=0
qi=0
for i in range(n):
    L.append(float(input('elementos: ')))
    if L[i]%2==0:
        p+=L[i]
        qp+=1
    else:
        i+=L[i]
        qi+=1
print(i)
print(p)
print(qi)
print(qp)
print(L)
        
        