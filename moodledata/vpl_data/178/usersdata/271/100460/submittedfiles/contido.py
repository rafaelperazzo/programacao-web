# -*- coding: utf-8 -*-
#ENTRADA
n = int(input('Digite a quantidade de termos da lista :'))
m = int(input('Digite a quantidade de termos da lista :'))
a = []
b = []
#PROCESSAMENTO
for i in range(0,n,1):
    valor_a = float(input('Digite o elemento da lista a: '))
    a.append(valor_a)
for i in range(0,m,1) :
    valor_b = float(input('Digite o elemento da lista b : '))
    b.append(valor_b)
#FUNÇÃO
def quantidade (lista) :
    k = 0
    cont = 0
    while (k<n) :
        for i in range (0,m,1) :
            if(a[k] == b[i]):
                cont = cont+1
        k = k+1
    return(cont)
#SAIDA
print (quantidade(a))
print (quantidade(b))


