# -*- coding: utf-8 -*-
n=0
m=0
while not n>=2 and n<=1000:
    n=int(input('N: '))
while not m>=2 and m<=1000:
    m=int(input('M: '))
matriz=[]
for i in range(0,n,1):
    linhas=[]
    for j in range(0,m,1):
        linhas.append(int(input("qual o valor da quadra %d,%d?" %(i+1,j+1))))
    matriz.append(linhas)
    

print(matriz)

for i in range(0,n,1):
    sum(matriz[i])
print(sum)




    

