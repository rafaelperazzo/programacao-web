# -*- coding: utf-8 -*-
M=int(input('Quantidade de quadras no sentido Norte-Sul: '))
while M<2 or M>=1000:
    M=int(input('Quantidade de quadras no sentido Norte-Sul: '))

N=int(input('Quantidade de quadras no sentido Leste-Oeste: '))
while N<2 or N>=1000:
    N=int(input('Quantidade de quadras no sentido Leste-Oeste: '))
    
v=[]
for i in range(M):
    quadra=[]
    for j in range(N):
        quadra.append(int(input('valor da quadra: ')))
        
r=[]
for i in range(M+1):
    for j in range(N+1):
        r.append(v[j][i])
        
print(r)
    
    
    
        

    