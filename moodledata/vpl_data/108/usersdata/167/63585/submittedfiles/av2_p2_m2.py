# -*- coding: utf-8 -*-
def vi(m,ent,sai):
    soma=0
    if sai>=ent:
        for i in range (ent,sai+1,1):
            soma=soma+m[i]
    else:
        for i in range (ent,sai-1,1):
            soma=soma+m[i]
    return soma

n=int(input('digite qnts salas: '))

m=[]
for i in range(0,n,1):
    valor=int(input('qnt de vi:'))
    m.append(valor)
 
ent=input('digite entrada:')
sai=input('digite saida:')

print(vi(m,ent,sai))
    