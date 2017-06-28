# -*- coding: utf-8 -*-
def  qtdvidas(pe,ps):
    soma=0
    for i in range (pe,ps+1,1):
        soma=soma+a[i]
    return(soma)

n=int(input('Quantidade de elementos da lista: '))
a=[]
for i in range (0,n,1):
    v=int(input('Quantidade de vidas: '))
    a.append(v)
pe=int(input('Qual porta de entrada: '))
ps=int(input('Qual porta de saida: '))
print(qtdvidas(pe,ps))


