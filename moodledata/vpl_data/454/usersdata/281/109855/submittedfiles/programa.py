# -*- coding: utf-8 -*-
c=int(input('Digite o número de consutas ao estoque: '))

l= []
feitos= []
for i in range(0,c,1):
    l.append(int(input('Digite o tamanho do  taco: ' )))

for i in range (0,c,1):
    if l[i] not in feitos:
        feitos.append(l[i])
        feitos.append(l[i])
        
print(len(feitos))
    
        