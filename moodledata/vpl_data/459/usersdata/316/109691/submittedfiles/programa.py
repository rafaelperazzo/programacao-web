# -*- coding: utf-8 -*-
nc=int(input('digite o numero de consultas: '))
e=[]
for x in range(0,nc,1):
    e.append(float(input('digite o tamanho do taco: ')))
e=sorted(set(e))
nt=len(e)*2
print(nt)
    
