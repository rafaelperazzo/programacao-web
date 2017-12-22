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
print(c)
print(ct)

    
