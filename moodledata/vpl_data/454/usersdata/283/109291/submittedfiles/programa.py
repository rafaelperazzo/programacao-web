# -*- coding: utf-8 -*-
C = int(input('Digite o número de consultas: '))
a=[]
for i in range(0,C,1):
    b=int(input('Digite o tamanho do taco: '))
    a.append(b)
print(a)
for j in range(0,C,1):
    if [j+1]==C:
        break
    if a[j]==a[j+1]:
        del a[j+1]

print(a)
        
