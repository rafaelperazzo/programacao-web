# -*- coding: utf-8 -*-
def max_deg(k):
    deg_k = []
    for i in range(0, len(k)-1):
        deg_k.append(abs(k[i]-k[i+1]))
    return max(deg_k)
############ - PROGRAMA PRINCIPAL - ############
n = int(input("Digite a quantidade de termos da lista: "))
k = []
for i in range(1, n+1):
    k.append(int(input("Digite o %dº elemento: "%i)))
print(max_deg(k))