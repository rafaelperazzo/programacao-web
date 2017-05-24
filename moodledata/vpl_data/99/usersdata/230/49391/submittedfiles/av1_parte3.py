# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite valor de n: '))
soma=1
i=1
j=0
for i in range(1,n+2,1):
    if i%3==1:
        soma=soma-1/(i*(3**j))
        j=j+1
        i=i+2
    else:
        soma=soma+1/(i*(3**j))
        j=j+1
        i=i+2
pi= (12**1/2)*soma
print('%.6f' %pi)