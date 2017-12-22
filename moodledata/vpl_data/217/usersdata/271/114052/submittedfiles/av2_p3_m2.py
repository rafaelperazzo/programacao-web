# -*- coding: utf-8 -*-
import numpy as np
#ENTRADA
m = int(input('Digite a dimensão : '))
a = np.zeros((m,m))
for i in range (0,a.shape[0],1) :
    for j in range(0,a.shape[1],1) :
        a[i,j] = int(input('Digite o elemento : '))
        
#FUNÇÕES
def soma1 (matriz,linha) :
    soma = 0
    for j in range (0,matriz.shape[1],1) :
        soma  = soma + matriz[linha,j]
    return (soma)

def soma2 (matriz,coluna) :
    soma = 0
    for i in range (0,matriz.shape[0],1) :
        soma = soma + matriz[i,coluna]
    return (soma)
#PROCESSAMENTO
soma = 0
soma3 = []
for i in range (0,a.shape[0],1) :
    soma = soma1(a,i)
    soma3.append(soma)

soma = 0
soma4 = []
for j in range (0,a.shape[1],1) :
    soma = soma2(a,j)
    soma4.append(soma)

x = []
y = []
for j in range (0,len(soma3),1) :
    if soma3[i] == soma3[j] :
        x.append(j)
    if soma3[i] != soma3[j] :
        y.append(j)
if len(x) > len(y) :
    linha_alterada = y[0]
else :
    linha_alterada = x[0]
    
z = []
w = []
for j in range (0,len(soma4),1) :
    if soma4[i] == soma4[j] :
        z.append(j)
    if soma4[i] != soma4[j] :
        w.append(j)
if len(z)>len(w) :
    coluna_alterada = w[0]
else :
    coluna_alterada = z[0]

altera = a[linha_alterada,coluna_alterada]
if linha_alterada == 0 :
    soma_b = soma1(a,1)
else :
    soma_b = soma1(a,linha_alterada)
soma_alterada = soma1(a,linha_alterada)
    
#SAIDA
sub = soma_alterada - soma_b
res = a[linha_alterada,coluna_alterada] - sub
print('%d' % res)
print ('%d' % a[linha_alterada,coluna_alterada])
    
    
            




