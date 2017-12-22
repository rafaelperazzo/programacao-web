# -*- coding: utf-8 -*-
def lecker(lista):
    cont = 0
    
    for i in range(0, len(lista)):
        if i == 0:
            if lista[0] > lista[1]:
                cont += 1
                
        elif i == (len(lista) - 1):
            if lista[len(lista)-1] > lista[len(lista)-2]:
                cont += 1
                
        else:
            if lista[i-1] < lista[i] > lista[i+1]:
                cont += 1
                
        del i
        
    if cont == 1:
        return "S"
        
    else:
        return "N"
        
########################### - PROGRAMA PRINCIPAL - ############################
n = int(input())
a, b = [], []
for i in range(0, n):
    a.append(int(input()))
    del i

for i in range(0, n):
    b.append(int(input()))
    del i
    
print(lecker(a))
print(lecker(b))

