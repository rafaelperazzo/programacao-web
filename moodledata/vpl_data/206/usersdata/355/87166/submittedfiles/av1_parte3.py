# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite n: '))
e=0
i=1
pi=0
for termo in range(1,n+1,1):
    if termo%2==0:
        pi=pi-(1/(i*(3**e)))
    else:
        pi=pi+(1/(i*(3**e)))
    e=e+1
    i=i+2
pi=pi*(12**(1/2))
print('%.6f'% pi)
        