# -*- coding: utf-8 -*-
M=int(input('Quantidade de quadras no sentido Norte-Sul: '))
while M<=2 or M>=1000:
    M=int(input('Quantidade de quadras no sentido Norte-Sul: '))

N=int(input('Quantidade de quadras no sentido Leste-Oeste: '))
while N<=2 or N>=1000:
    N=int(input('Quantidade de quadras no sentido Leste-Oeste: '))
    
v=[]
for i in range(M):
    quadra=[]
    for j in range(N):
        quadra.append(int(input('valor da quadra: ')))
        
mt=[]
for i in range(N):
    r=[]
    for j in range(M):
        r.append(v[j][i])
    mt.append(r)
      
  
s=1000
for i in range(N):
    if sum(mt[i])<s:
        s=sum(mt[i])
print(s)

    
    
    
        

    