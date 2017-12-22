# -*- coding: utf-8 -*-
list=[]
n=int(input('Digite a quantidade de termos da lista: '))
for i in range(0,n,1):
    num=int(input('Digite um numero para a lista: '))
    list.append(num)

soma1=0
cont1=0
soma2=0
cont2=0
for num in range(0,n,1):
    if (list[num])%2==0:
        soma1=soma1+(list[num])
        cont1=cont1+1
    else:
        soma2=soma2+(list[num])
        cont2=cont2+1

print(soma1)
print(soma2)
print(cont1)
print(cont2)
print(list)



