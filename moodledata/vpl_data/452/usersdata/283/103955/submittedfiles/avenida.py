# -*- coding: utf-8 -*-
M=int(input('M: '))
N=int(input('N: '))

while(M<2 or M>1000):
    print('Digite outro valor M')
    M=int(input('M: '))
while(N<2 or N>1000):
    print('Digite outro valor N')
    N=int(input('N: '))
a=[]

for i in range(M-1,-1,-1):
    l=[]
    for j in range(N-1,-1,-1):
        l.append(int(input('Digite o valor da quadra: ')))
    a.append(l)
x=[]

for k in range(-1,M-1,1):
    if sum(a[k]) < sum(a[k+1]):
        x.append(sum(a[k]))
    if (k+1)>M-1:
        break
g=[]
for l in range(-1,len(x)-1,1):
    for c in range(0,len(x)-1,1):
        if x[l]<x[c]:
            g.append(x[l])
print(g[0])
    
        
    