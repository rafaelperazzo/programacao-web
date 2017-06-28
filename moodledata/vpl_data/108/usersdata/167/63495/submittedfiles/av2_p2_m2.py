# -*- coding: utf-8 -*-
def vi(m,ent,sai):
    soma=0
    if sai>=ent:
        for i in range (ent,sai+1,1):
            soma=soma+m[i]
    if ent>sai:
        for i in range (ent,sai-1,-1):
            soma=soma+m[i]
    return soma

for i in range(0,n,1):
    m.append(int(input('digite qnt vida sala:'))

n=input('digite qnts salas: ')
m=[]
ent= int(input('digite entrada:'))
sai= int(input('digite saida:'))

print (vi(m,b,c))
    