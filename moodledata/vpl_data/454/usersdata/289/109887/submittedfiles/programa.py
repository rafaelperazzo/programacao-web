# -*- coding: utf-8 -*-
n=int(input("Digite o número de consultas ao estoque: "))
m=[]
for i in range(0,n,1):
    m.append(int(input("Digite o tamanho do taco%.d: " %(i+1))))
c=sorted(m)
cont=0
for i in range(1,n,1):
    if c[i-1]==c[i]:
        cont+=1
x=((len(c)-cont)*2)
print(x)



