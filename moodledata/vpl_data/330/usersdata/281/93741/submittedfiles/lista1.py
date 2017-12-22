# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de valores que você quer : '))
a=[]
for i in range(0,n,1):
    a.append(int(input('Digite os valores: ')))
sp=0
si=0
qi=0
qp=0
for i in range(0,n,1):
    if a[i] % 2 == 0:
        qp = qp+1
        sp =sp+a[i]
    else:
        si=si+1
        qi=qi+a[i]
print(si)
print(sp)
print(qi)
print(qp)
    
    
        
        
        
        
        

