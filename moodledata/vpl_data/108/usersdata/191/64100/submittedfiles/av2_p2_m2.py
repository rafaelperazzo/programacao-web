# -*- coding: utf-8 -*-
def jogo(lista,entrada,saida):
    soma=0
    if sai>=entrada:
        for i in range(entrada,saida+1,1):
            soma=soma+lista[i]
        else:
            for i in range(entrada,saida-1,1):
                soma=soma+lista[i]
        return soma
        
n=int(input('digite n:'))
a=[]
for i in range(0,n,1):
    valor=int(input('quantidade de vidas:'))
    a.append(valor)
entrada=int(input('entrada:'))
saida=int(input('saida:'))
print(jogo(a,entrada,saida))

