# -*- coding: utf-8 -*-
C = int(input('Digite o número de consultas: '))
a=[]
for i in range(0,C,1):
    b=int(input('Digite o tamanho do taco: '))
    a.append(b)
c=sorted(a)
d=[]
for j in range(0,C,1):
    if [j+1] == C:
        break
    if a[j]==a[j+1]:
        d.append(a[j+1])
for k in range(0,len(d),1):
    a.remove(d[k])
print(a)
    
    
        
