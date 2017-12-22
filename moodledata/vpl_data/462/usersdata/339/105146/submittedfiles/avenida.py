# -*- coding: utf-8 -*-
M=int(input('Quantidade de quadras no sentido Norte-Sul: '))
while M<2 or M>=1000:
    M=int(input('Quantidade de quadras no sentido Norte-Sul: '))

N=int(input('Quantidade de quadras no sentido Leste-Oeste: '))
while N<2 or N>=1000:
    N=int(input('Quantidade de quadras no sentido Leste-Oeste: '))
    
v=[]
for i in range(M):
    quadras=[]
    for j in range(N):
        quadra.append(int(input('valor da quadra: ')))
        
r=[]
for i in range(M):
    for j in range(N):
        r.append(v[j][i])
        
sr=[]
for t in range(len(r)-1):
    sr.append(sum(r[t]))
    
for i in range(len(sr)-1):
    if sr[i]>sr[i+1] and sr[i]>sr[i-1]:
        print(sr[i])
    elif sr[i]>sr[i+1] and sr[i]<sr[i-1]:
        print(sr[i-1])
    elif sr[i]<sr[i+1] and sr[i]>sr[i-1]:
        print(sr[i+1])
    
    
    
        

    