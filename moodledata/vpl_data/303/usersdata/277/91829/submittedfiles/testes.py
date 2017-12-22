def inserir(vetor,valor,n) :
    vetor.append(0.0)
    for i in range(len(vetor)-1,0,-1):
        if (i==n) :
            vetor[i] = valor
        else :
            vetor[i] = vetor[i-1]
    return vetor
    
# -*- coding: utf-8 -*-
a = [8.0, 5.0, 10.0, 5.0]
print(a)
print(len(a))
# 2.0 na posicao 2 (indice 1)
inserir(a,2.0,1)
print(a)
print(len(a))


#for i in range(2 , -1 , -1):
#    print(a[i])