# -*- coding: utf-8 -*-
def jogo(lista,entra,sai):
    soma=0
    if sai>=entra:
        for i in range(entra,sai+1,1):
            soma=soma+lista[i]
        else:
            for i in range(entra,sai-1,1):
                soma=soma+lista[i]
        return soma
        
n=int(input('digite n:'))
a=[]
for i in range(0,n,1):
    valor=int(input('quantidade de vidas:'))
    a.append(valor)
entra=int(input('entrada:'))
sai=int(input('saida:'))
print(jogo(a,entra,sai))

