# -*- coding: utf-8 -*-

while True:
    M=int(input('Quantidade de quadras no sentido Norte-Sul: '))
    if  M>=2 and M<=1000:
        break

while True:
    N=int(input('Quantidade de quadras no sentido Leste-Oeste: '))
    if  N>=2 and N<=1000:
        break
    
v=[]
for i in range(M):
    quadra=[]
    for j in range(N):
        quadra.append(int(input('valor da quadra: ')))
    v.append(quadra[i][j])
        
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

    
    
    
        

    