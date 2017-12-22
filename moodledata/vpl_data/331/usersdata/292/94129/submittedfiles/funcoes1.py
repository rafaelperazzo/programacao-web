# -*- coding: utf-8 -*-

def cres(k):
    cont = 0
    
    for i in range(0, len(k)-1):
        if k[i] < k[i+1]:
            cont += 1
            
    if cont == len(k)-1:
        return "S"
        
    else:
        return "N"

def decres(k):
    cont = 0
    
    for i in range(0, len(k)-1):
        if k[i] > k[i+1]:
            cont += 1
            
    if cont == len(k)-1:
        return "S"
        
    else:
        return "N"
        
def cons(k):
    cont = 0
    
    for i in range(0, len(k)-1):
        if k[i] == k[i+1]:
            cont += 1
            
    if cont != 0:
        return "S"
        
    else:
        return "N"
        
############## - PROGRAMA PRINCIPAL - ############

n = int(input("Digite a quantidade de elementos: "))
l1, l2, l3 = [], [], []

for j in range(1, n+1):
    l1.append(int(input("Digite o %dº elemento da 1º lista: "%j )))
    
for j in range(1, n+1):
    l2.append(int(input("Digite o %dº elemento da 2º lista: "%j )))

for j in range(1, n+1):
    l3.append(int(input("Digite o %dº elemento da 3º lista: "%j )))

print(cres(l1))
print(decres(l1))
print(cons(l1))

print(cres(l2))
print(decres(l2))
print(cons(l2))

print(cres(l3))
print(decres(l3))
print(cons(l3))
        