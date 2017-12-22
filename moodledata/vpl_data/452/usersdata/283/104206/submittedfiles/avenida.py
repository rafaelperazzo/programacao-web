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

for k in range(0,M,1):
    if (k+1)==M:
        break
    if sum(a[k]) < sum(a[k+1]):
        x.append(sum(a[k]))
    
g=[]
for l in range(0,len(x),1):
    for c in range(0,len(x),1):
        if x[l]<x[c]:
            g.append(x[l])
w=[]

for y in range(0,N,1):
    q=[]
    for u in range(0,M,1):
        q.append(a[u][y])
    w.append(q)
print(w)
h=[]
for r in range(0,len(w),1):
    if (r+1)==len(w):
        break
    if sum(w[r]) < sum (w[r+1]):
        h.append(sum(w[r]))
e=[]
for z in range(0,len(h),1):
    for t in range (0,len(h),1):
        if h[z]<h[t]:
            e.append(h[z])
    
print(e)
        
        
        


    
        
    