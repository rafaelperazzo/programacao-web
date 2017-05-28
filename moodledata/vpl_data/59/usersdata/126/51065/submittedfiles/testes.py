# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n=int(input('digite o numero:'))

p=0
q=n
cont=0
i=0

while q!=0:
    q=q//10
    cont=cont+1
    for i in range(1,cont+1,1):
        soma=0
        while n>0:
            p=n%10
            n=n//10
            soma=soma+p**2
        n=soma
        i=i+1
if soma==1:
    print('S')
else:
    print('N')
print(soma)   
print(cont)
        