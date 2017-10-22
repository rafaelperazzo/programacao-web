# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
n=int(input('Digite a quantidade de termos: '))
i=1
soma=0
exp=0
while exp<n:
    if ex%2==0:
        soma=soma+(1/(i*(3**exp)))
    else:
        soma=soma-(1/(i*(3**exp)))
i=i+2
exp=exp+1
pi=(12**(0.5))*soma
print ('%.6f' %pi)