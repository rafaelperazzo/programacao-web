# -*- coding: utf-8 -*-
def vi(m,ent,sai):
    soma=0
    if sai>=ent:
        for i in range (ent,sai+1,1):
            soma=soma+m[i]
    if ent>sai:
        for i in range (ent,sai-1,1):
            soma=soma+m[i]
    return soma

n=input('digite qnts salas:')
x=[]
ent=int(input('digite entrada:'))
sai=int(input('digite saida:'))

for i in range(0,n,1):
    x.append(int(input('digite qnt vida sala:'))


print (vi(m,b,c))
    