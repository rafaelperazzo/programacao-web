# -*- coding: utf-8 -*-
def tacos(consultas):
    verificacao = []
    cont = 0
    for i in consultas:
        ver = 0
        for j in verificacao:
            if i == j:
                ver += 1
                
            del j
        
        if ver%2 == 0:
            cont += 2
            
        del i
            
    return cont
    
####################### - PROGRAMA PRINCIPAL - #######################
C = int(input("Digite o número de consultas ao estoque: "))
consultas = []
for i in range(1, C+1):
    consultas.append(int(input("Digite o valor da %dº consulta: "%i)))
    
    del i
    
print(tacos(consultas))