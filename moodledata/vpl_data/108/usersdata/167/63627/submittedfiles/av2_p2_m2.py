# -*- coding: utf-8 -*-
def jogo(lista,ent,sai):
    soma=0
    if sai>=ent:
        for i in range(ent,sai+1,1):
            soma=soma+lista[i]
    else:
        for i in range (ent,sai-1,1):
            soma=soma+lista[i]
    return soma
n=int(input('digite n:'))
lista=[]
for i in range (0,n,1):
    valor=int(input('qnt de vi em cada sala:'))
    lista.append(valor)
ent=int(input('ent:'))
sai=int(input('sai:'))
print(jogo(lista,ent,sai))
    