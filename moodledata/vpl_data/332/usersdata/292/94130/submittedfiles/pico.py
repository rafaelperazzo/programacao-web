# -*- coding: utf-8 -*-

def pic(j):
    cont, cont1 = 0, 0
    for i in range(2, len(j)+1):
        k1 = j[:i]
        k2 = []
        for k in k1:
            k2.append(k)
        k1.sort()
        if (k1 == k2):
            cont = i
            
        else:
            break
        
    for i in range(1, len(j)):
        if (j[i] == j[i-1]):
            cont1 += 1
            
    if (cont == 0) or (cont == len(j)) or (cont1 != 0):
        return "N"
        
    else:
        k3 = j[cont-1:]
        k4 = []
        for k in k3:
            k4.append(k)
        k3.sort()
        k3.reverse()
        if (k3 == k4):
            return "S"
            
        else:
            return "N"
            
############ - PROGRAMA PRINCIPAL - ##########
k = []
n = int(input("Digite a quantidade de elementos da lista: "))
for i in range(1, n+1):
    an = int(input("Digite o %dº elemento: "%i))
    k.append(an)
    
print(pic(k))