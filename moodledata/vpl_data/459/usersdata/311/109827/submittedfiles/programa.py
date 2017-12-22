# -*- coding: utf-8 -*-
ntacos=[]
tacosfeitos=0
consultas=int(input('Digite o numero de consultas: '))
for i in range (0,consultas,1):
    taco=int(input('Digite o comprimento: '))
    if taco in ntacos:
        ntacos.remove(taco)
    else:
        tacosfeitos=tacosfeitos+2
        ntacos.append(taco)
print (tacosfeitos)
    
