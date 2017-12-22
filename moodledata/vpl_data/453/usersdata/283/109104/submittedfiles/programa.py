# -*- coding: utf-8 -*-
a=[]
b=int(input('Digite a dimensão do tabuleiro: '))
while b<=0:
    print('Digite outro valor')
    b=int(input('Digite a dimensão do tabuleiro: '))
a.append(b)
c=[]
for i in range(0,b,1):
    l=[]
    for j in range(0,b,1):
        l.append(int(input('Digite um número para a linha %d: ' %i)))
    c.append(l)
ct=[]
for g in range(0,b,1):
    s=[]
    for h in range(0,b,1):
        s.append(c[h][g])
    ct.append(s)
y=[]
for k in range(0,b,1):
    for v in range(0,b,1):
        y.append(sum(c[k]) + sum(ct[v]) - 2*c[k][v])
o=[]
for x in range(0,len(y),1):
    if (y[x] <= y[x+1]):
        o.append(y[x])
    if(y[x+1] == len(y)):
        break
while len(o)>1:
    for u in range(0,len(o),1):
        if o[u] <= o[u+1]:
            o.pop(u+1)
        if (u+1)==(len(o)):
            
        

        
    

    
